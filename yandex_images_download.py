import time
import logging
import pathlib
import sys
import os

from multiprocessing import Pool
from downloader import YandexImagesDownloader, get_driver, download_single_image, save_json
from parse import parse_args


def scrap(args):
    keywords = []
    criteria=False

    #flagsShortened
    isd=args.image_same_directory
    kw=args.keywords
    kwf=args.keywords_from_file

    if isd:
        criteria=True
        keywords.extend(
            [ item for item in os.listdir("./putYourImagesHere") ]
        )
    elif kw:
        keywords.extend([
                    str(item).strip() for item in args.keywords.split(",") if len(item)
                ])
    elif kwf:
        with open(args.keywords_from_file, "r") as f:
                keywords.extend([line.strip() for line in f])
    else:
        raise Exception(f"Only one of the input flags should be used")     
            
    
   
    driver = get_driver(args.browser, args.driver_path)

    try:
        downloader = YandexImagesDownloader(driver, args.output_directory,
                                            args.limit, args.isize,
                                            args.exact_isize, args.iorient,
                                            args.extension, args.color,
                                            args.itype, args.commercial,
                                            args.recent, None)

        start_time = time.time()
        total_errors = 0

        if keywords:
            
            downloader_result = downloader.download_images(keywords,searchByImage=criteria)
            total_errors += sum(
                keyword_result.errors_count
                for keyword_result in downloader_result.keyword_results)
        
    finally:
        driver.quit()
        

    total_time = time.time() - start_time

    logging.info("\nEverything downloaded!")
    logging.info(f"Total errors: {total_errors}")
    logging.info(
        f"Total files downloaded: {len(keywords) * args.limit - total_errors}")
    logging.info(f"Total time taken: {total_time} seconds.")
    

def setup_logging(quiet_mode):
    logging.basicConfig(level=logging.WARNING if quiet_mode else logging.INFO,
                        format="%(message)s")
    selenium_logger = logging.getLogger('seleniumwire')
    selenium_logger.setLevel(logging.WARNING)


def main():
    try:
        args = parse_args()
        setup_logging(args.quiet_mode)
        scrap(args)

    except KeyboardInterrupt as e:
        logging.error("KeyboardInterrupt")
        sys.exit(1)

    except Exception as e:
        logging.error(e, exc_info=True)
        sys.exit(1)


main()
