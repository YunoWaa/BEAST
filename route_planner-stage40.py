# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: RoutePlanner
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='RoutePlanner CLI')
    sub = parser.add_subparsers(dest='command')

    # point
    p = sub.add_parser('point', help='create a point')
    p.add_argument('name', type=str)
    p.add_argument('--lat', type=float, required=True)
    p.add_argument('--lon', type=float, required=True)
    p.add_argument('--desc', type=str, default='')

    # task
    p = sub.add_parser('task', help='create a task')
    p.add_argument('point_name', type=str)
    p.add_argument('--description', type=str, required=True)
    p.add_argument('--priority', type=int, default=5)
    p.add_argument('--due', type=str, default='')
    p.add_argument('--done', type=bool, default=False)

    # route
    p = sub.add_parser('route', help='create a route')
    p.add_argument('--name', type=str, required=True)
    p.add_argument('--waypoints', type=str, nargs='+', required=True)

    # note
    p = sub.add_parser('note', help='add a road note')
    p.add_argument('--point_name', type=str, required=True)
    p.add_argument('--text', type=str, required=True)
    p.add_argument('--color', type=str, default='gray')

    # list
    sub.add_parser('list', help='list all items')

    return parser.parse_args()
