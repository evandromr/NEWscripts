#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""A simple tool to download an RXTE observation from the HEASARC archive
   Author: Evandro M. Ribeiro <ribeiro .at. astro.rug.nl>
   Last updated: 18 Nov 2015 by Author
"""
import argparse
from ftplib import FTP


def download_xte_obs(obsid, user='anonymous', passwd='anonymous@server.com'):
    """
    download_xte_obs(obsid, user='anonymous', passwd='anonymous@server.com')

    Download a RXTE observation from HEASARC archive via FTP
    The function identifies the location of the observation's files by the 
    number of the obseration ID and download all the files as a compressed
    *tar.gz file

    Parameters
    ----------
    obsid: str
        Observation ID to download
    user: str, optional
        User name for ftp connection. default is 'anonymous'
    passwd: str, optional
        Password for ftp connection. default is 'anonymous@server.com'

    Returns
    -------
    None: None

    Notes
    -----
    The observation will be saved as  <obsid>.tar.gz file in the current directory

    The default password is a dummy e-mail adress, HEASARC asks users to use their
    own e-mail as password, please provide your real e-mail when downloading. (See examples below).

    Examples
    --------
    1. As a command line tool: Downloading as anonymous
    
    $ get_xte_obs.py 5081-02-56-98 -p username@mail.com
    
    2. As a command line tool: Downloading as username
    
    $ get_xte_obs.py 5081-02-56-98 -u username -p username@mail.com
    
    1. - Inside a python script: Downloading as username

    >>> from get_xte_obs import download_xte_obs
    >>> obsid = '95081-02-56-98'
    >>> my_user = 'username'
    >>> my_password = '1234'
    >>> download_xte_obs(obsid, my_user, my_password)

    2. - Inside a python script: Downloading as anonymous
         Username is `anonymous` by default, your e-mail is the password
   
    >>> from get_xte_obs import download_xte_obs
    >>> obsid = '95081-02-56-98'
    >>> my_password = 'username@mail.com'
    >>> download_xte_obs(obsid, passwd=my_password)

    """

    pid = obsid[:5]
    # Calculates AO number according to obsid
    if int(pid[:2]) < 90:
        ao = 'AO'+pid[0]
    else:
        ao = 'AO'+str(int(pid[1])+9)

    # P-id of the observation according to obsid
    pid = 'P'+pid

    # obsid to download as a tar.gz file
    tarfile = obsid+'.tar.gz'

    # start  FTP connection
    ftp = FTP('heasarc.gsfc.nasa.gov')
    ftp.login(user, passwd)

    # set debug level to moderate
    ftp.debuglevel(1)

    # path to obsid
    path = "/xte/data/archive/"+ao+"/"+pid

    # move to folder
    ftp.cwd(path)

    print('Attempting to download file {0}'.format(path+'/'+tarfile))
    print('Please Wait... This could take long depending on the download')

    # get file
    ftp.retrbinary('RETR {0}'.format(tarfile), open(tarfile, 'wb').write)
    print('File {0} Sucessfully downloaded'.format(tarfile))

    # quit FTP connection
    ftp.quit()


if __name__ == "__main__":

    # Get arguments from command line if runing as a script
    parser = argparse.ArgumentParser()
    parser.add_argument('obsid', help="The ObsID to be downloaded.")
    parser.add_argument('-u', '--user', help="User for ftp connection")
    parser.add_argument('-p', '--passwd', help="Password for ftp connection. \
                        HEASARC asks for your e-mail adress if user is \
                        anonymous")

    args = parser.parse_args()

    # check if login as anonymous or with user/passwd
    if args.user or args.passwd:
        download_xte_obs(args.obsid, args.user, args.passwd)
    else:
        download_xte_obs(args.obsid, args.user, args.passwd)
