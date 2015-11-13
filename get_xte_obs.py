#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import argparse
from ftplib import FTP


def download_xte_obs(obsid, user='anonymous', passwd='anonymous@server.com'):
    """
    download_xte_obs(obsid, user='anonymous', passwd='anonymous@server.com')

    Download a RXTE observation from HEASARC archive via FTP

    Parameters
    ----------
    obsid: str
        Observation ID to download
    user: str
        User name for ftp connection. default is 'anonymous'
    passwd: str
        Password for ftp connection. default is 'anonymous@server.com'

    Returns
    -------
    None: None

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

    return None


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
