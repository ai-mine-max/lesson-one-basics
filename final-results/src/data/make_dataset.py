# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    logger.info(input_filepath)
    logger.info(output_filepath)

def read_matlab_x_cgpauc(filename_txt):
    """Prepares x_cgpauc.mat data for trainngi

    Args:
        filename_txt (Object): represents file name for the unprocessed file
    """
    


if __name__ == '__main__':
    LOG_FMT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=LOG_FMT)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]
    INPUT_FILE, OUTPUT_FILE = 2, 3
    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main(INPUT_FILE, OUTPUT_FILE)
