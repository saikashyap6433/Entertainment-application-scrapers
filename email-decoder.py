#Email Decoder for Cloudflare encrypted emails
import argparse
import netflixaccountscrapers.lib.processing as processing

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Program to decode email \
        protection from files/servers managed with Cloudflare.", epilog="It can \
         identify generally when you find the string '[email protected]'.")

    groupIO = parser.add_mutually_exclusive_group(required=True)
    groupIO.add_argument("-f", "--file", help="Input file to replace emails protected")
    groupIO.add_argument("-u", "--uri", help="URI to download and replace emails protected")

    groupInfo = parser.add_mutually_exclusive_group()
    groupInfo.add_argument("-v", "--verbose", action="store_true")

    args = parser.parse_args()

    processing.ced_main(args)
