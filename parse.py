import argparse

parser = argparse.ArgumentParser( description='Process some integers.')
parser = argparse.ArgumentParser()
parser.add_argument('--foo', action='append')
parser.parse_args()

args = parser.parse_args()
args.error("died")
