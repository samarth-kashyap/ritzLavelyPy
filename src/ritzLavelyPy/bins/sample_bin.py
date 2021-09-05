#!/usr/bin/env python

from ritzLavelyPy import ritzLavelyPoly

def main():
    """Sample function that creates a Ritzwoller-Lavely polynomial"""
    ell, jmax = 100, 5
    RLP = ritzLavelyPoly(ell, jmax)
    return None

if __name__ == "__main__":
    main()
