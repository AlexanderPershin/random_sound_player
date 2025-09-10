import os
import logging
import random
import pygame
from time import sleep

log = logging.getLogger('sound_player')
logging.basicConfig(level=logging.DEBUG)


class SoundPlayer:
    """
    class to play random sounds from directory at random intervals
    """

    def __init__(
        self,
        delay_start: int = 5,
        delay_end: int = 10,
        dir_name: str = 'sounds',
        show_log: bool = True,
    ):
        self._delay_start = delay_start
        self._delay_end = delay_end
        self._dir_name = dir_name
        if not show_log:
            log.propagate = False

    def __call__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(1.0)

        filenames = os.listdir(self._dir_name)
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
    player = SoundPlayer()
    player()


if __name__ == '__main__':
    main()
