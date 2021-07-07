parser = argparse.ArgumentParser()
#parser.add_argument('-i', '--input', required=True, 
#                    help='path to the input data')
parser.add_argument('-t', '--threshold', default=0.965, type=float,
                    help='score threshold for discarding detection')
args = vars(parser.parse_args())
