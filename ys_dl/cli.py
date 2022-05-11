from ys_dl import __version__
import fire


class YsDlCli:
    @staticmethod
    def version():
        return __version__


def main():
    fire.Fire(YsDlCli)


if __name__ == '__main__':
    main()
