import math
from scipy.special import erf, erfc, erfcinv

# Ported from https://wismuth.com/elo/calculator.html
# https://chessprogramming.wikispaces.com/Pawn+Advantage,+Win+Percentage,+and+ELO
FIDE_STDEV = 2000 / 7

FIRST_MOVER_ADVANTAGE = .2
DRAW_ODDS_ADVANTAGE = .325  # .6


def elo_fn(elo_diff):
    return erfc(-elo_diff / (FIDE_STDEV * math.sqrt(2))) / 2

def inv_elo_fn(p):
    return -(FIDE_STDEV * math.sqrt(2)) * erfcinv(p * 2)

def add_elo(diff, delta):
    if diff * delta >= 0:
        return diff + delta

    if diff > 0:
        return -inv_elo_fn(2 * elo_fn(-diff) - elo_fn(-diff + delta))
    else:
        return inv_elo_fn(2 * elo_fn(diff) - elo_fn(diff - delta))

class Elo:
    def __init__(self, white_advantage=.1, draw_odds_advantage=.6):
        self.white_advantage = white_advantage
        self.draw_odds_advantage = draw_odds_advantage

    def shifted_diffs(self, white_elo, black_elo):
        diff = white_elo - black_elo
        avg_elo = (white_elo + black_elo) / 2
        elo_per_pawn = math.exp((avg_elo - 3720) / 1020) * 1020

        c1 = elo_per_pawn * self.white_advantage
        c2 = elo_per_pawn * self.draw_odds_advantage

        diff_w = add_elo(diff, c1 - c2)
        diff_wh = add_elo(diff, c1 + c2)
        return (diff_w, diff_wh)

    def elo_diff(self, white_elo, black_elo):
        diff_w, diff_wh = self.shifted_diffs(white_elo, black_elo)

        if diff_w > 0:
            return -inv_elo_fn((elo_fn(-diff_w) + elo_fn(-diff_wh)) / 2)
        else:
            return inv_elo_fn((elo_fn(diff_w) + elo_fn(diff_wh)) / 2)

    def material_adjustment(self, white_elo, black_elo):
        avg_elo = (white_elo + black_elo) / 2
        elo_per_pawn = math.exp((avg_elo - 3720) / 1020) * 1020
        delta = self.elo_diff(avg_elo, avg_elo)
        return delta / elo_per_pawn

    def material_from_elo(self, elo):
        return -math.exp(-(elo - 3720) / 1020)

    def material_odds(self, white_elo, black_elo):
        diff_material = self.material_from_elo(white_elo) - self.material_from_elo(black_elo)
        return diff_material + self.material_adjustment(white_elo, black_elo)

    def draw_probability(self, white_elo, black_elo):
        diff_w, diff_wh = self.shifted_diffs(white_elo, black_elo)
        return elo_fn(diff_wh) - elo_fn(diff_w)

    def probabilities(self, white_elo, black_elo):
        escore = elo_fn(int(self.elo_diff(white_elo, black_elo)))
        draw_prob = self.draw_probability(white_elo, black_elo)
        white_win_prob = escore - draw_prob / 2
        black_win_prob = 1 - white_win_prob - draw_prob
        return {'white': white_win_prob, 'black': black_win_prob, 'draw': draw_prob}


def material_odds(white_elo, black_elo):
    elo = Elo()
    diff_material = elo.material_from_elo(white_elo) - elo.material_from_elo(black_elo)
    return diff_material + elo.material_adjustment(white_elo, black_elo)

def probabilities(white_elo, black_elo):
    return Elo().probabilities(white_elo, black_elo)
