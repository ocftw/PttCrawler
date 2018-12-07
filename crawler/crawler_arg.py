import argparse
from utils import valid_date_type


def get_base_parser() -> argparse.ArgumentParser:
    base_subparser = argparse.ArgumentParser(add_help=False)
    base_subparser.add_argument('--debug-mode',
                                action='store_true')
    base_subparser.add_argument('--verbose',
                                action='store_true',
                                help='Show more debug messages.')
    base_subparser.add_argument('--config-path',
                                type=str,
                                help='Config ini file path.')
    base_subparser.add_argument('--version',
                                action='version',
                                version='%(prog)s 1.0')
    return base_subparser


def add_article_arg_parser(parser: argparse.ArgumentParser):

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--start-date',
                       type=valid_date_type,
                       help='start datetime in format "YYYY-MM-DD"')
    group.add_argument('--index',
                       type=int,
                       metavar=('START_INDEX', 'END_INDEX'),
                       nargs=2)
    parser.add_argument('--board-name',
                        type=str.lower,
                        required=True)
    # Output
    parser.add_argument('--json-folder',
                        type=str,
                        default='')
    parser.add_argument('--json-prefix',
                        type=str,
                        default='')


def add_asn_arg_parser(parser: argparse.ArgumentParser):
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument('--ip-list',
                             type=str)
    input_group.add_argument('--database', action='store_true')


def add_user_arg_parser(parser: argparse.ArgumentParser):
    # user id input
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--id',
                       type=str)
    group.add_argument('--database', action='store_true')

    # Output
    parser.add_argument('--json-prefix',
                        type=str,
                        default='')
