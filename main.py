import os
import argparse
import logging
import random
from time import sleep

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

log = logging.getLogger('SOUND_PLAYER')
logging.basicConfig(level=logging.DEBUG)


class SoundPlayer:
    """
    class to play random sounds from directory at random intervals
    """

    def __init__(
        self,
        dir_name: str = 'sounds',
        delay_start: int = 5,
        delay_end: int = 10,
        show_log: bool = True,
    ):
        if delay_end <= delay_start or delay_start < 0 or delay_end < 0:
            raise ValueError('Delay start/end should be positive integers')

        self._dir_name = dir_name
        self._delay_start = delay_start
        self._delay_end = delay_end

        if not show_log:
            log.propagate = False

    def __call__(self):
        import pygame

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(1.0)

        filenames = os.listdir(self._dir_name)
        log.info(f'reading directory: {self._dir_name}...')
        log.info(f'loaded files: {", ".join(filenames)}')
        try:
            while True:
                filename = random.choice(filenames)
                delay = random.randint(self._delay_start, self._delay_end)
                log.info(f'using {filename}...')
                pygame.mixer.music.load(os.path.join(self._dir_name, filename))
                pygame.mixer.music.play(1)
                log.info(f'sleeping for {delay} seconds...')
                sleep(delay)
        except KeyboardInterrupt:
            log.info('\nexiting...')


def main():
    parser = argparse.ArgumentParser(
        description='A simple random sound playing program.'
    )
    parser.add_argument(
        '--dir', type=str, default='sounds', help='Sounds direcotry'
    )
    parser.add_argument(
        '--start', type=int, default=5, help='Sound play delay range start'
    )
    parser.add_argument(
        '--end', type=int, default=10, help='Sound play delay range end'
    )
    parser.add_argument(
        '--verbose', action='store_true', help='Show logs while running'
    )

    args = parser.parse_args()
    dir_name = args.dir
    delay_start = args.start
    delay_end = args.end
    verbose = args.verbose

    player = SoundPlayer(
        dir_name=dir_name,
        delay_start=delay_start,
        delay_end=delay_end,
        show_log=verbose,
    )
    player()


if __name__ == '__main__':
    main()
