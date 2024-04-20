/*
SQLyog Community Edition- MySQL GUI v7.15 
MySQL - 5.5.29 : Database - fn
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`fn` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `fn`;

/*Table structure for table `cloud` */

DROP TABLE IF EXISTS `cloud`;

CREATE TABLE `cloud` (
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `cloud` */

insert  into `cloud`(`username`,`password`) values ('cloud','cloud');

/*Table structure for table `owner` */

DROP TABLE IF EXISTS `owner`;

CREATE TABLE `owner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `owner` */

insert  into `owner`(`id`,`username`,`password`,`email`,`address`) values (2,'raj','raj','raj@gmail.com','hyderabad');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fname` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `ctext` varchar(100) DEFAULT NULL,
  `uemail` varchar(100) DEFAULT NULL,
  `msg` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`id`,`fname`,`email`,`ctext`,`uemail`,`msg`,`status`) values (3,'abc.txt','raj@gmail.com','B4ofFtkZ34qm/EqGi1EK6slmMx2hxbFTLsZo0PjyKhc=','moulalicce225@gmail.com','genuine','keysent');

/*Table structure for table `upload` */

DROP TABLE IF EXISTS `upload`;

CREATE TABLE `upload` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `fname` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `data` varchar(100) DEFAULT NULL,
  `skey` varchar(100) DEFAULT NULL,
  `ctext` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `status1` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `upload` */

insert  into `upload`(`id`,`fname`,`email`,`data`,`skey`,`ctext`,`status`,`status1`) values (5,'abc.txt','raj@gmail.com','hii helloo how are you','l3VpJsCDRjtlamp110IIEg==','B4ofFtkZ34qm/EqGi1EK6slmMx2hxbFTLsZo0PjyKhc=','uploadtocloud','genuine');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`id`,`username`,`password`,`email`,`address`) values (1,'chotu','chotu','moulalicce225@gmail.com','hyderabad');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
