

import sys
import re
import requests
import logging

def request_file(uri):
    """
    Make a request and return its content

    Args:
        uri (string): The URI with the protected content

    Returns:
        object: Response object
    """
    r = requests.get(uri, stream=True, headers={"User-Agent": 'CED'})
    return r


def decode_email(encodedString):
    """
    Receive a string and process its value to make it readable

    Args:
        encodedString (string): The encoded email with CoudFlare CDN protection

    Returns:
        string: The decoded email
    """
    r = int(encodedString[:2],16)
    email = ''.join([chr(int(encodedString[i:i+2], 16) ^ r) for i in range(2,
        len(encodedString), 2)])
    return email
    #print(email)


def replace_content(text, decode=False):
    """
    Check the links with regular expression to find encoded content
    and replace it

    Args:
        text (string): Text to check
        decode (bool, optional): Set to decode content with utf-8 codification
    """
    emailregex = 'data-cfemail=\"([^\"]+)\"'
    tagregex = r'<a href="\/cdn-cgi\/l\/email-protection"[^>]*>([^<]+)<\/a>'
    for line in text:
        if decode:
            line = line.decode('utf-8')
        m = re.search(emailregex,line)
        if m:
            line = re.sub(tagregex, decode_email(m.group(1)), line)
        #print(line)
            #sys.stdout=open("hulu_output.txt","w")
            #print(line)
            #email.email_fetch()
        #f.close()

def ced_main(args):
    """
    Main function called by launcher
    """
    logger = logging.getLogger('CED')
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    logger.info("Starting ced-launcher.py ...")

    # With input file
    if args.file:
        logger.info("Trying to open the input file ...")

        try:
            lines = [line.rstrip('\n') for line in open(args.file)]
            replace_content(lines)
            logger.info("The replacements were done successfully")
        except Exception as e:
            #sys.exit("ERROR: Ensure you have permission to read the input file.")

    # With URI
    elif args.uri:
        logger.info("Trying to get the content of the requested URI ...")

        try:
            replace_content(request_file(args.uri), True)
            logger.info("The replacements were done successfully")
        except Exception as e:
            #sys.exit("ERROR: Ensure you have permission to write the output file.")
