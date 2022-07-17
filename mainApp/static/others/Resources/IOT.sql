-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jul 15, 2022 at 09:01 PM
-- Server version: 8.0.29-0ubuntu0.20.04.3
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `IOT`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(3, 'administrator'),
(5, 'operator'),
(1, 'supervisorgudang'),
(4, 'supervisorppic'),
(2, 'supervisorproduksi');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_group_permissions`
--

INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
(1, 1, 25),
(2, 1, 26),
(3, 1, 27),
(4, 1, 28),
(5, 1, 29),
(6, 1, 30),
(7, 1, 31),
(8, 1, 32),
(9, 1, 33),
(10, 1, 34),
(11, 1, 35),
(12, 1, 36),
(13, 1, 37),
(14, 1, 38),
(15, 1, 39),
(16, 1, 40),
(17, 1, 41),
(18, 1, 42),
(19, 1, 43),
(20, 1, 44),
(21, 1, 45),
(22, 1, 46),
(23, 1, 47),
(24, 1, 48),
(25, 1, 49),
(26, 1, 50),
(27, 1, 51),
(28, 1, 52),
(29, 1, 53),
(30, 1, 54),
(31, 1, 55),
(32, 1, 56),
(33, 1, 57),
(34, 1, 58),
(35, 1, 59),
(36, 1, 60),
(37, 2, 25),
(38, 2, 26),
(39, 2, 27),
(40, 2, 28),
(41, 2, 29),
(42, 2, 30),
(43, 2, 31),
(44, 2, 32),
(45, 2, 33),
(46, 2, 34),
(47, 2, 35),
(48, 2, 36),
(49, 2, 37),
(50, 2, 38),
(51, 2, 39),
(52, 2, 40),
(53, 2, 41),
(54, 2, 42),
(55, 2, 43),
(56, 2, 44),
(57, 2, 45),
(58, 2, 46),
(59, 2, 47),
(60, 2, 48),
(61, 2, 49),
(62, 2, 50),
(63, 2, 51),
(64, 2, 52),
(65, 2, 53),
(66, 2, 54),
(67, 2, 55),
(68, 2, 56),
(69, 2, 57),
(70, 2, 58),
(71, 2, 59),
(72, 2, 60);

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add logging', 7, 'add_logging'),
(26, 'Can change logging', 7, 'change_logging'),
(27, 'Can delete logging', 7, 'delete_logging'),
(28, 'Can view logging', 7, 'view_logging'),
(29, 'Can add print header', 8, 'add_printheader'),
(30, 'Can change print header', 8, 'change_printheader'),
(31, 'Can delete print header', 8, 'delete_printheader'),
(32, 'Can view print header', 8, 'view_printheader'),
(33, 'Can add product', 9, 'add_product'),
(34, 'Can change product', 9, 'change_product'),
(35, 'Can delete product', 9, 'delete_product'),
(36, 'Can view product', 9, 'view_product'),
(37, 'Can add register', 10, 'add_register'),
(38, 'Can change register', 10, 'change_register'),
(39, 'Can delete register', 10, 'delete_register'),
(40, 'Can view register', 10, 'view_register'),
(41, 'Can add department', 11, 'add_department'),
(42, 'Can change department', 11, 'change_department'),
(43, 'Can delete department', 11, 'delete_department'),
(44, 'Can view department', 11, 'view_department'),
(45, 'Can add report title', 12, 'add_reporttitle'),
(46, 'Can change report title', 12, 'change_reporttitle'),
(47, 'Can delete report title', 12, 'delete_reporttitle'),
(48, 'Can view report title', 12, 'view_reporttitle'),
(49, 'Can add uploaded register', 13, 'add_uploadedregister'),
(50, 'Can change uploaded register', 13, 'change_uploadedregister'),
(51, 'Can delete uploaded register', 13, 'delete_uploadedregister'),
(52, 'Can view uploaded register', 13, 'view_uploadedregister'),
(53, 'Can add report', 14, 'add_report'),
(54, 'Can change report', 14, 'change_report'),
(55, 'Can delete report', 14, 'delete_report'),
(56, 'Can view report', 14, 'view_report'),
(57, 'Can add weighing state', 15, 'add_weighingstate'),
(58, 'Can change weighing state', 15, 'change_weighingstate'),
(59, 'Can delete weighing state', 15, 'delete_weighingstate'),
(60, 'Can view weighing state', 15, 'view_weighingstate'),
(61, 'Can add report register', 16, 'add_reportregister'),
(62, 'Can change report register', 16, 'change_reportregister'),
(63, 'Can delete report register', 16, 'delete_reportregister'),
(64, 'Can view report register', 16, 'view_reportregister'),
(65, 'Can add access list', 17, 'add_accesslist'),
(66, 'Can change access list', 17, 'change_accesslist'),
(67, 'Can delete access list', 17, 'delete_accesslist'),
(68, 'Can view access list', 17, 'view_accesslist');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$320000$xNqQhSKXYYJwHuTS5SABgE$mpYbX3/8UhDXBvzoqtqfUUPseQC3jkJ6xLM7wDNWwBI=', '2022-07-15 14:06:35.931132', 1, 'admin', '', '', 'admin@admin.com', 1, 1, '2022-03-22 08:12:32.689091'),
(2, 'pbkdf2_sha256$320000$5GKoodTu5XjSmIyYvUAIAf$hNjqtQ74EKWAxI4Uh5pvUqHWeLTQeuCDIVyovVSAi1s=', NULL, 0, 'supervisorproduksiiiii', '', '', '', 0, 1, '2022-05-23 02:47:47.303653'),
(3, 'pbkdf2_sha256$320000$OndA9cKLkPQiMqwKTuIMWx$uv3UF4fARQdtu19z4OLAuzBUWHWywF+K7ztt1ppN5FE=', '2022-06-09 06:44:40.520576', 0, 'supervisorgudang', '', '', '', 0, 1, '2022-05-23 02:48:12.236025'),
(4, 'pbkdf2_sha256$320000$94OZMw1zJESZWCW22mQD9V$Z5iubIdeNZzCghhEDrVwFokjQSxykzHL+GJEoAvJ2DI=', '2022-07-14 15:19:32.097681', 0, 'spvgudang', '', '', '', 0, 1, '2022-06-21 08:40:21.106634'),
(5, 'pbkdf2_sha256$320000$ZtHn9DP7UKMJ88UvFLzAAk$QazfyJhUYBtnKL0Dual2GAZE359vIwkJAMVs7zmEsgI=', '2022-07-14 15:23:10.893193', 0, 'spvprod', '', '', '', 0, 1, '2022-06-21 08:42:29.050169'),
(6, 'pbkdf2_sha256$320000$zXqcgHsMyIiTBhbYjECGeQ$q3tUXjsYgR3bxQ2Hh/7CcFXnqU5zow9bHeZxyP2q40A=', '2022-07-14 15:34:31.725918', 0, 'spvppic', '', '', '', 0, 1, '2022-07-05 09:02:28.086902'),
(7, 'pbkdf2_sha256$320000$ABOcrNDpIpfd447E0QQ1yr$dOwY/pbdmVnHUyhJP9hH0pt358GVbMbfvOYBZfZ+t5I=', NULL, 0, 'operator1', '', '', '', 0, 1, '2022-07-05 11:09:47.958327');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_user_groups`
--

INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(5, 1, 3),
(2, 2, 2),
(10, 3, 1),
(7, 4, 1),
(9, 5, 2),
(6, 6, 4),
(8, 7, 5);

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL
) ;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2022-05-23 02:48:56.468561', '1', 'supervisorgudang', 1, '[{\"added\": {}}]', 3, 1),
(2, '2022-05-23 02:49:17.587278', '2', 'supervisorproduksi', 1, '[{\"added\": {}}]', 3, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(11, 'mainApp', 'department'),
(7, 'mainApp', 'logging'),
(8, 'mainApp', 'printheader'),
(9, 'mainApp', 'product'),
(10, 'mainApp', 'register'),
(14, 'mainApp', 'report'),
(16, 'mainApp', 'reportregister'),
(12, 'mainApp', 'reporttitle'),
(13, 'mainApp', 'uploadedregister'),
(15, 'mainApp', 'weighingstate'),
(17, 'secureapp', 'accesslist'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-03-22 08:10:46.475274'),
(2, 'auth', '0001_initial', '2022-03-22 08:10:47.958216'),
(3, 'admin', '0001_initial', '2022-03-22 08:10:48.353737'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-03-22 08:10:48.445313'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-03-22 08:10:48.522919'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-03-22 08:10:48.846438'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-03-22 08:10:48.987695'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-03-22 08:10:49.106966'),
(9, 'auth', '0004_alter_user_username_opts', '2022-03-22 08:10:49.159610'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-03-22 08:10:49.334291'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-03-22 08:10:49.354966'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-03-22 08:10:49.484189'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-03-22 08:10:49.591182'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-03-22 08:10:49.647343'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-03-22 08:10:49.707131'),
(16, 'auth', '0011_update_proxy_permissions', '2022-03-22 08:10:49.833629'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-03-22 08:10:49.906713'),
(18, 'mainApp', '0001_initial', '2022-03-22 08:10:50.532388'),
(19, 'sessions', '0001_initial', '2022-03-22 08:10:50.644351'),
(20, 'mainApp', '0002_product_status', '2022-04-01 06:10:35.389796'),
(21, 'mainApp', '0003_auto_20220323_2247', '2022-04-01 06:16:23.089164'),
(22, 'mainApp', '0004_auto_20220323_2301', '2022-04-01 06:16:23.175148'),
(23, 'mainApp', '0005_alter_product_status', '2022-04-01 06:16:23.186622'),
(24, 'mainApp', '0006_department_report_reporttitle_uploadedregister', '2022-04-01 06:16:23.679084'),
(25, 'mainApp', '0007_uploadedregister_product', '2022-04-01 06:16:23.845871'),
(26, 'mainApp', '0008_uploadedregister_measuredate', '2022-04-01 06:16:23.907173'),
(27, 'mainApp', '0009_auto_20220331_0855', '2022-04-01 06:16:23.999049'),
(28, 'mainApp', '0010_auto_20220406_1959', '2022-04-06 13:28:58.417634'),
(29, 'mainApp', '0011_auto_20220415_0210', '2022-04-25 01:19:21.334318'),
(30, 'mainApp', '0012_productstate_status', '2022-04-25 01:19:21.397216'),
(31, 'mainApp', '0013_rename_productstate_weighingstate', '2022-04-25 01:19:21.479802'),
(32, 'mainApp', '0014_alter_register_status', '2022-04-25 01:19:21.645293'),
(33, 'mainApp', '0015_weighingstate_batchno', '2022-04-25 01:19:21.734535'),
(34, 'mainApp', '0016_auto_20220419_1208', '2022-04-25 01:19:22.062202'),
(35, 'mainApp', '0017_auto_20220420_2031', '2022-04-25 01:19:22.345802'),
(36, 'mainApp', '0018_auto_20220420_2034', '2022-04-25 01:19:22.599722'),
(37, 'mainApp', '0019_weighingstate_pendingstatus', '2022-05-23 02:45:29.981435'),
(38, 'mainApp', '0020_alter_weighingstate_pendingstatus', '2022-05-23 02:45:30.008107'),
(39, 'mainApp', '0021_auto_20220518_0924', '2022-05-23 02:45:30.562632'),
(40, 'mainApp', '0022_auto_20220521_2247', '2022-05-23 02:45:30.624483'),
(41, 'mainApp', '0023_alter_register_weight', '2022-06-03 08:14:27.369113'),
(42, 'mainApp', '0024_alter_register_weight', '2022-06-03 08:14:27.574172'),
(43, 'mainApp', '0025_remove_register_product', '2022-06-17 10:55:31.333042'),
(44, 'mainApp', '0026_remove_register_productbatchnoboxno', '2022-06-17 10:55:31.435362'),
(45, 'mainApp', '0027_register_product', '2022-06-17 10:55:31.758704'),
(46, 'mainApp', '0028_auto_20220616_1528', '2022-06-17 10:55:32.673941'),
(47, 'secureapp', '0001_initial', '2022-07-05 08:19:09.395234'),
(48, 'secureapp', '0002_auto_20220627_1032', '2022-07-05 08:19:10.168390'),
(49, 'secureapp', '0003_alter_accesslist_feature_name', '2022-07-05 08:19:10.320918');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('2queo37r6vn8zkvf7gk84r1gr4jck1ff', '.eJxVjEEOwiAQRe_C2hDoAC0u3XsGMsyAVA0kpV0Z765NutDtf-_9lwi4rSVsPS1hZnEWWpx-t4j0SHUHfMd6a5JaXZc5yl2RB-3y2jg9L4f7d1Cwl2-dMyYVOdrRaBdHzRnRsAUiY73x5CaVlEHQyAAJfGZGNw2aBoToIIv3BwxdOK4:1o1eHn:X5o0j6RmWelGTcboMAuDlcLgCh1KR7JMpOG6wCkQLXc', '2022-06-30 01:27:03.233768'),
('6skx76adfg2e81psreh5ixxjyeeey60o', '.eJxVjEEOwiAQRe_C2hDoAC0u3XsGMsyAVA0kpV0Z765NutDtf-_9lwi4rSVsPS1hZnEWWpx-t4j0SHUHfMd6a5JaXZc5yl2RB-3y2jg9L4f7d1Cwl2-dMyYVOdrRaBdHzRnRsAUiY73x5CaVlEHQyAAJfGZGNw2aBoToIIv3BwxdOK4:1o1KJC:lplZWHSJb3fGxak9zq_mo4oJWEnbpFCxItul9LLFYqA', '2022-06-29 04:07:10.735425'),
('aumq4aq4ogf04m91xc9fklbrr3x2u6nk', '.eJxVjEEOwiAQRe_C2hDoAC0u3XsGMsyAVA0kpV0Z765NutDtf-_9lwi4rSVsPS1hZnEWWpx-t4j0SHUHfMd6a5JaXZc5yl2RB-3y2jg9L4f7d1Cwl2-dMyYVOdrRaBdHzRnRsAUiY73x5CaVlEHQyAAJfGZGNw2aBoToIIv3BwxdOK4:1nocJN:f5_k9bGX35TiE4WhNT09nnaq7Mv54u9oaJ8WmhA-po4', '2022-05-25 02:42:49.058748'),
('gby5fqvptgrll3aa8gbj8y8bxs9wrrxb', '.eJxVjEEOwiAQRe_C2hDoAC0u3XsGMsyAVA0kpV0Z765NutDtf-_9lwi4rSVsPS1hZnEWWpx-t4j0SHUHfMd6a5JaXZc5yl2RB-3y2jg9L4f7d1Cwl2-dMyYVOdrRaBdHzRnRsAUiY73x5CaVlEHQyAAJfGZGNw2aBoToIIv3BwxdOK4:1oBoPO:TWmGErYhO9K0p9KR6JfWg6yK9yYyWP2Ixinr0xCg828', '2022-07-28 09:16:54.370443'),
('o0zfdqbeoyeywqdgdx68xouqwqjt51gh', '.eJxVjEEOwiAQRe_C2hDoAC0u3XsGMsyAVA0kpV0Z765NutDtf-_9lwi4rSVsPS1hZnEWWpx-t4j0SHUHfMd6a5JaXZc5yl2RB-3y2jg9L4f7d1Cwl2-dMyYVOdrRaBdHzRnRsAUiY73x5CaVlEHQyAAJfGZGNw2aBoToIIv3BwxdOK4:1ncI9K:UXqKqLt4mibL4AxiBSBhAQ_uI-dkLiBbLzsedu3JajA', '2022-04-21 02:45:30.275058'),
('o7s1isxmqqexf94ddxaswa3tzegmp1kk', '.eJxVjEEOwiAQRe_C2hDoAC0u3XsGMsyAVA0kpV0Z765NutDtf-_9lwi4rSVsPS1hZnEWWpx-t4j0SHUHfMd6a5JaXZc5yl2RB-3y2jg9L4f7d1Cwl2-dMyYVOdrRaBdHzRnRsAUiY73x5CaVlEHQyAAJfGZGNw2aBoToIIv3BwxdOK4:1nc8Ww:X3z7C6nmASwSQVhlj8WpQ1MkF57cWEiJD7vy-mTBIEM', '2022-04-20 16:29:14.364542'),
('pscljyupeohdug04czadmhp3pbzlbrnm', '.eJxVjEEOwiAQRe_C2hDoAC0u3XsGMsyAVA0kpV0Z765NutDtf-_9lwi4rSVsPS1hZnEWWpx-t4j0SHUHfMd6a5JaXZc5yl2RB-3y2jg9L4f7d1Cwl2-dMyYVOdrRaBdHzRnRsAUiY73x5CaVlEHQyAAJfGZGNw2aBoToIIv3BwxdOK4:1o1LSM:QzAoncHQp2lAoinXH2OhdRez05vRWXJqdD_arJtMF9U', '2022-06-29 05:20:42.612808'),
('q023aq0o0bw834ehae38zzvsk5uxxcu3', '.eJxVjEEOwiAQRe_C2hDoAC0u3XsGMsyAVA0kpV0Z765NutDtf-_9lwi4rSVsPS1hZnEWWpx-t4j0SHUHfMd6a5JaXZc5yl2RB-3y2jg9L4f7d1Cwl2-dMyYVOdrRaBdHzRnRsAUiY73x5CaVlEHQyAAJfGZGNw2aBoToIIv3BwxdOK4:1oCExa:BNKlMd4fQIoaxzzKbbtXeGnFGgokm98NjzYiOhtkr-4', '2022-07-29 13:37:58.262553'),
('vrhus05sh7mvjrl8f6er6sjdnx51x5op', '.eJxVjEEOwiAQRe_C2hDoAC0u3XsGMsyAVA0kpV0Z765NutDtf-_9lwi4rSVsPS1hZnEWWpx-t4j0SHUHfMd6a5JaXZc5yl2RB-3y2jg9L4f7d1Cwl2-dMyYVOdrRaBdHzRnRsAUiY73x5CaVlEHQyAAJfGZGNw2aBoToIIv3BwxdOK4:1nqskA:Qv6wVm7o-ynyoX70cb9KrEfB_K2nLrkdvaZ50QYNed0', '2022-05-31 08:39:50.982103'),
('yekxggsuco2r3d7kmt0dylufwvj3fyed', '.eJxVjEEOwiAQRe_C2hDoAC0u3XsGMsyAVA0kpV0Z765NutDtf-_9lwi4rSVsPS1hZnEWWpx-t4j0SHUHfMd6a5JaXZc5yl2RB-3y2jg9L4f7d1Cwl2-dMyYVOdrRaBdHzRnRsAUiY73x5CaVlEHQyAAJfGZGNw2aBoToIIv3BwxdOK4:1nWZjZ:cS_cOE5ZCAMiOgxrgiMD6aObDG9zdb-c-tsvK9Cwaco', '2022-04-05 08:19:17.710621'),
('zpzxh0c973vs1om3z34zh8y5xwx5q113', '.eJxVjEEOwiAQRe_C2hDoAC0u3XsGMsyAVA0kpV0Z765NutDtf-_9lwi4rSVsPS1hZnEWWpx-t4j0SHUHfMd6a5JaXZc5yl2RB-3y2jg9L4f7d1Cwl2-dMyYVOdrRaBdHzRnRsAUiY73x5CaVlEHQyAAJfGZGNw2aBoToIIv3BwxdOK4:1nWee9:cAcW32a-1jrLOWmFt10KZmJBqEUI3ZXPTDAbCIY17ac', '2022-04-05 13:34:01.325874');

-- --------------------------------------------------------

--
-- Table structure for table `Logging`
--

CREATE TABLE `Logging` (
  `Id` int NOT NULL,
  `Datetime` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `Lot` int DEFAULT NULL,
  `Status` int DEFAULT NULL,
  `Weighing` float(9,4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Logging`
--

INSERT INTO `Logging` (`Id`, `Lot`, `Status`, `Weighing`) VALUES
(59618, 12345, 1, 30000.0000),
(713845, 1, 1, 34.6000),
(713853, 1, 1, 130.0000),
(713860, 1, 1, 195.4000),
(1083887, 0, 2, 5375.0000),
(1083888, 1, 2, 5375.0000),
(1083889, 2, 2, 5690.0000),
(1083890, 3, 3, 5688.0000),
(1083891, 4, 1, 5688.0000),
(1083892, 5, 1, 5690.0000),
(1083893, 6, 1, 5690.0000),
(1083894, 7, 1, 5374.0000),
(1083895, 8, 1, 5374.0000),
(1083896, 9, 1, 5374.0000),
(1083897, 0, 1, 5373.0000),
(1083898, 1, 1, 5373.0000),
(1083899, 0, 1, 5374.0000),
(1083900, 1, 1, 5684.0000),
(1083901, 2, 1, 5690.0000),
(1083902, 3, 2, 5374.0000),
(1083903, 4, 3, 5690.0000),
(1083904, 5, 3, 5686.0000),
(1083905, 6, 3, 5690.0000),
(1083906, 7, 2, 5691.0000),
(1083907, 8, 2, 5691.0000),
(1083908, 9, 2, 5691.0000),
(1083909, 10, 2, 5690.0000),
(1083910, 11, 2, 5689.0000),
(1083911, 12, 3, 5690.0000),
(1083912, 13, 1, 5690.0000),
(1083913, 14, 1, 5690.0000),
(1083914, 0, 1, 5375.0000),
(1083915, 1, 1, 5692.0000),
(1083916, 2, 1, 5765.0000),
(1083917, 3, 1, 5375.0000),
(1083918, 4, 1, 5376.0000),
(1083919, 5, 1, 5375.0000),
(1083920, 0, 1, 5374.0000),
(1083921, 1, 1, 5374.0000),
(1083922, 2, 1, 5374.0000),
(1083923, 3, 1, 5374.0000),
(1083924, 4, 1, 5374.0000),
(1083925, 5, 1, 5691.0000),
(1083926, 6, 1, 5691.0000),
(1083927, 7, 1, 5374.0000),
(1083928, 8, 1, 5692.0000),
(1083929, 9, 1, 5376.0000),
(1083930, 10, 3, 1201.5000),
(1083931, 11, 1, 5692.0000),
(1083932, 12, 1, 5375.0000),
(1083933, 13, 1, 5691.0000),
(1083934, 14, 1, 6085.0000),
(1083935, 15, 1, 5374.0000),
(1083936, 16, 1, 6086.0000),
(1083937, 17, 1, 5375.0000),
(1083938, 18, 1, 6086.0000),
(1083939, 19, 1, 5374.0000),
(1083940, 20, 1, 5374.0000),
(1083941, 21, 3, 1533.6000),
(1083942, 22, 2, 1533.5000),
(1083943, 23, 3, 1533.9000),
(1083944, 24, 3, 1534.5000),
(1083945, 25, 2, 1534.3000),
(1083946, 26, 1, 5375.0000),
(1083947, 27, 1, 5692.0000),
(1083948, 28, 3, 1532.8000),
(1083949, 29, 1, 5692.0000),
(1083950, 30, 1, 5375.0000),
(1083951, 31, 2, 1533.0000),
(1083952, 32, 2, 1533.0000),
(1083953, 33, 3, 1532.9000),
(1083954, 0, 3, 1534.4000),
(1083955, 1, 2, 1534.3000),
(1083956, 2, 2, 5374.0000),
(1083957, 3, 1, 5691.0000),
(1083958, 4, 2, 1534.8000),
(1083959, 5, 2, 1534.5000),
(1083960, 1, 1, 1550.0000),
(1083961, 6, 1, 5375.0000),
(1083962, 7, 1, 5691.0000),
(1083963, 1, 1, 3000.0000),
(1083964, 1, 1, 3001.0000),
(1083965, 1, 2, 3002.0000),
(1083966, 1, 1, 3020.1230),
(1083967, 1, 10, 10.0000),
(1083968, 1, 1, 3002.0000),
(1083969, 1, 2, 3002.5000),
(1083970, 1, 0, 3002.8000),
(1083971, 0, 2, 703.2000),
(1083972, 1, 1, 5000.0000),
(1083973, 1, 2, 7000.0000),
(1083974, 1, 0, 8000.0000),
(1083975, 1, 2, 2000.0000),
(1083976, 1, 1, 3000.0000),
(1083977, 1, 0, 8000.0000),
(1083978, 1, 3, 3000.0000),
(1083979, 0, 3, 703.7000),
(1083980, 1, 2, 703.5000),
(1083981, 2, 3, 703.5000),
(1083982, 3, 3, 703.5000),
(1083983, 4, 3, 693.5000),
(1083984, 5, 3, 703.5000),
(1083985, 6, 3, 703.5000),
(1083986, 7, 3, 703.5000),
(1083987, 8, 3, 693.7000),
(1083988, 9, 3, 703.2000),
(1083989, 10, 3, 703.0000),
(1083990, 11, 2, 693.7000),
(1083991, 12, 3, 693.4000),
(1083992, 13, 3, 703.5000),
(1083993, 14, 3, 703.5000),
(1083994, 15, 3, 693.5000),
(1083995, 16, 3, 703.5000),
(1083996, 17, 3, 693.4000),
(1083997, 18, 3, 703.5000),
(1083998, 19, 3, 693.4000),
(1083999, 20, 3, 703.5000),
(1084000, 21, 3, 608.5000),
(1084001, 22, 2, 703.5000),
(1084002, 23, 2, 693.5000),
(1084003, 24, 2, 693.5000),
(1084004, 25, 3, 703.5000),
(1084005, 26, 3, 693.5000),
(1084006, 27, 3, 703.5000),
(1084007, 28, 3, 693.5000),
(1084008, 29, 3, 693.5000),
(1084009, 30, 3, 703.7000),
(1084010, 31, 3, 693.5000),
(1084011, 32, 3, 703.5000),
(1084012, 33, 3, 693.5000),
(1084013, 34, 3, 703.4000),
(1084014, 35, 3, 693.0000),
(1084015, 36, 3, 703.4000),
(1084016, 37, 3, 693.2000),
(1084017, 38, 3, 693.0000),
(1084018, 39, 3, 533.0000),
(1084019, 40, 3, 693.5000),
(1084020, 41, 3, 533.2000),
(1084021, 42, 3, 693.2000),
(1084022, 43, 3, 532.9000),
(1084023, 44, 3, 693.0000),
(1084024, 45, 3, 532.9000),
(1084025, 46, 3, 618.7000),
(1084026, 47, 3, 533.0000),
(1084027, 48, 3, 693.2000),
(1084028, 49, 3, 532.7000),
(1084029, 50, 3, 693.0000),
(1084030, 1, 1, 450.0000),
(1084031, 1, 2, 5000.0000),
(1084032, 0, 2, 532.9000),
(1084033, 0, 1, 532.7000),
(1084034, 1, 1, 532.9000),
(1084035, 2, 1, 532.7000),
(1084036, 3, 1, 532.7000),
(1084037, 4, 1, 532.5000),
(1084038, 5, 1, 532.9000),
(1084039, 6, 1, 532.7000),
(1084040, 7, 1, 532.9000),
(1084041, 8, 1, 532.7000),
(1084042, 9, 1, 532.7000),
(1084043, 10, 1, 532.5000),
(1084044, 11, 1, 532.7000),
(1084045, 12, 2, 1112.8000),
(1084046, 13, 2, 1112.8000),
(1084047, 14, 3, 1112.8000),
(1084048, 15, 3, 1112.8000),
(1084049, 16, 2, 1112.6000),
(1084050, 17, 1, 532.5000),
(1084051, 18, 1, 532.7000),
(1084052, 19, 1, 532.7000),
(1084053, 20, 1, 532.7000),
(1084054, 21, 1, 532.5000),
(1084055, 22, 3, 532.7000),
(1084056, 23, 1, 532.7000),
(1084057, 24, 2, 532.7000),
(1084058, 25, 1, 532.7000),
(1084059, 26, 1, 532.7000),
(1084060, 27, 1, 532.7000),
(1084061, 28, 1, 532.5000),
(1084062, 29, 1, 532.5000),
(1084063, 30, 1, 532.5000),
(1084064, 31, 1, 532.7000),
(1084065, 32, 1, 532.5000),
(1084066, 33, 1, 532.7000),
(1084067, 34, 1, 532.5000),
(1084068, 35, 1, 532.5000),
(1084069, 36, 2, 532.0000),
(1084070, 37, 3, 532.4000),
(1084071, 38, 1, 532.2000),
(1084072, 39, 1, 532.5000),
(1084073, 0, 2, 532.7000),
(1084074, 0, 2, 532.4000),
(1084075, 1, 3, 736.0000),
(1084076, 2, 3, 532.5000),
(1084077, 0, 1, 532.5000),
(1084078, 0, 1, 532.4000),
(1084079, 1, 3, 736.0000),
(1084080, 2, 1, 532.4000),
(1084081, 3, 1, 532.4000),
(1084082, 4, 1, 532.4000),
(1084083, 5, 2, 735.9000),
(1084084, 0, 1, 532.4000),
(1084085, 1, 1, 532.2000),
(1084086, 2, 2, 735.9000),
(1084087, 3, 1, 532.5000),
(1084088, 4, 2, 736.0000),
(1084089, 5, 3, 736.2000),
(1084090, 6, 1, 532.4000),
(1084091, 7, 2, 735.7000),
(1084092, 8, 2, 736.0000),
(1084093, 9, 2, 736.0000),
(1084094, 10, 2, 673.7000),
(1084095, 11, 1, 532.2000),
(1084096, 12, 1, 532.2000),
(1084097, 13, 1, 532.2000),
(1084098, 14, 1, 532.2000),
(1084099, 15, 1, 532.2000),
(1084100, 16, 1, 532.2000),
(1084101, 17, 2, 736.0000),
(1084102, 18, 1, 532.4000),
(1084103, 19, 1, 532.2000),
(1084104, 20, 3, 1111.9000),
(1084105, 21, 2, 1111.5000),
(1084106, 22, 3, 1111.5000),
(1084107, 23, 3, 736.0000),
(1084108, 24, 1, 532.2000),
(1084109, 25, 1, 532.0000),
(1084110, 26, 2, 736.2000),
(1084111, 27, 1, 735.9000),
(1084112, 28, 3, 1145.4000),
(1084113, 29, 2, 1145.4000),
(1084114, 0, 3, 1145.5000),
(1084115, 1, 3, 1145.5000),
(1084116, 2, 3, 566.0000),
(1084117, 3, 1, 736.0000),
(1084118, 0, 3, 1145.5000),
(1084119, 0, 2, 1145.5000),
(1084120, 1, 2, 1145.5000),
(1084121, 2, 3, 1145.3000),
(1084122, 3, 1, 736.0000),
(1084123, 0, 3, 1145.5000),
(1084124, 1, 2, 1145.5000),
(1084125, 2, 2, 566.0000),
(1084126, 3, 1, 735.9000);

-- --------------------------------------------------------

--
-- Table structure for table `mainApp_department`
--

CREATE TABLE `mainApp_department` (
  `id` int NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mainApp_department`
--

INSERT INTO `mainApp_department` (`id`, `name`) VALUES
(1, 'DEMAND SUPPY & SYSTEM DEPARTMENT'),
(2, 'DS&S'),
(3, 'PRODUKSI');

-- --------------------------------------------------------

--
-- Table structure for table `mainApp_printheader`
--

CREATE TABLE `mainApp_printheader` (
  `id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `label` varchar(20) NOT NULL,
  `imageurl` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `mainApp_product`
--

CREATE TABLE `mainApp_product` (
  `id` int NOT NULL,
  `name` varchar(100) NOT NULL,
  `code` varchar(30) NOT NULL,
  `createdon` datetime(6) NOT NULL,
  `updatedon` datetime(6) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `maxweight` double NOT NULL,
  `minweight` double NOT NULL,
  `standardweight` double NOT NULL,
  `createdby_id` int NOT NULL,
  `updatedby_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mainApp_product`
--

INSERT INTO `mainApp_product` (`id`, `name`, `code`, `createdon`, `updatedon`, `status`, `maxweight`, `minweight`, `standardweight`, `createdby_id`, `updatedby_id`) VALUES
(1, 'ALCOCLIN 5 L', 'ALCCL5L---', '2022-04-06 20:35:52.817071', '2022-06-17 01:19:40.835007', 1, 6, 4, 5, 1, 1),
(2, 'ALCOCLIN 50 ML', 'ALCL50----', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 12, 9, 10, 1, 1),
(3, 'ALCOCLIN 500 ML', 'ALCOLIN500', '2022-04-06 20:35:52.817071', '2022-07-15 15:09:24.833109', 1, 740, 730, 5, 1, 1),
(4, 'ALCOCLIN SWAB', 'ALCLSWAB--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 6.3, 4.3, 5.3, 1, 1),
(5, 'ALCOKIT SWAB', 'ALCKTSWAB-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 6.26, 4.26, 5.26, 1, 1),
(6, 'AMLODIPINE BESILATE KAPLET 10 MG', 'IFAMLO10--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3, 1, 2, 1, 1),
(7, 'AMLODIPINE BESILATE KAPLET 5 MG', 'IFAMLO5---', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4, 2, 3, 1, 1),
(8, 'ASCORBIC ACID IM/IV/SC 1G/5ML', 'ASCORACID1', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 6.99, 4.99, 5.99, 1, 1),
(9, 'ATORVASTATIN CALCIUM TRIHYDRATE KSS 40 mg', 'IATOR40---', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3.04, 1.04, 2.04, 1, 1),
(10, 'AZITHROMYCIN KSS 500 MG', 'IAZITR500K', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3, 1, 2, 1, 1),
(11, 'AZITHROMYCIN SIRUP KERING 200 mg/5 ml ', 'IAZITHROSK', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 9.89, 7.89, 8.89, 1, 1),
(12, 'BI 12 INJEKSI 500 MCG', 'BI12INJ---', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4.28, 2.28, 3.38, 1, 1),
(13, 'BIOFIN TSS 2.5 MG', 'BIOFIN2.5-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3.95, 1.95, 2.95, 1, 1),
(14, 'BIOFIN TSS 5 MG', 'BIOFIN5---', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3.95, 1.95, 2.95, 1, 1),
(15, 'BISOPROLOL FUMARATE TSS 2.5 MG', 'IBSPRL2.5-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3.95, 1.95, 2.95, 1, 1),
(16, 'BISOPROLOL FUMARATE TSS 5 MG', 'IBSPRL5---', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3.95, 1.95, 2.95, 1, 1),
(17, 'BITSWIT SIRUP ORANGE 100 ML', 'BITSWTORG-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 9, 7, 8.6, 1, 1),
(18, 'BITSWIT SIRUP STRAWBERRY 100 ML', 'BITSWTSRW-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5, 4.5, 1, 1, 1),
(19, 'BROXFION ELIXIR 15 MG/5 ML', 'BROXFION15', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 8.64, 6.64, 7.64, 1, 1),
(20, 'BROXFION ELIXIR 30 MG/5 ML', 'BROXFION30', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 8.55, 6.55, 7.55, 1, 1),
(21, 'BROXFION TABLET 30 MG', 'BROXF30TAB', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5, 4, 5, 1, 1),
(22, 'BUPION SPINAL HEAVY INJEKSI 0.5%', 'BUPONEKKAM', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5, 4.7, 5, 1, 1),
(23, 'CALCIUM CARBONAT KAP 500 MG', 'CACAR500--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 11, 10, 1, 1, 1),
(24, 'CALMOR TABLET KUNYAH', 'CALMORTAB-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3.75, 3.5, 3.66, 1, 1),
(25, 'CALREN KAPLET 500 MG', 'CARLEN500-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2.7, 1, 2, 1, 1),
(26, 'CANDEFION TABLET 16 mg', 'CNDFION16T', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2.92, 2.32, 2.62, 1, 1),
(27, 'CANDEFION TABLET 8 mg', 'CNDFION8T-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2.92, 2.32, 2.62, 1, 1),
(28, 'CANDESARTAN CILEXETIL TABLET 16 mg', 'ICNDE16TAB', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2.92, 2.32, 2.62, 1, 1),
(29, 'CANDESARTAN CILEXETIL TABLET 8 mg', 'ICNDE8TAB-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2.92, 2.32, 2.62, 1, 1),
(30, 'CARTIFIT TSS', 'CARTIFTTSS', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1, 1, 1, 1),
(31, 'CEFADROXIL MONOHYDRATE KAPSUL 500 mg', 'ICFDRX500K', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 8.46, 6.46, 7.46, 1, 1),
(32, 'CEFEPIME HCl SERBUK INJEKSI 1 g', 'ICEFEP1I--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4.36, 2.36, 3.36, 1, 1),
(33, 'CEFIXIME TRIHYDRATE KAPLET SALUT SELAPUT 200 mg', 'ICEFIX200-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4.12, 2.12, 3.12, 1, 1),
(34, 'CEFOPERAZONE SODIUM-SULBACTAM SODIUM SI 1 g', 'ICEFOBAC--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5.6, 3.6, 4.6, 1, 1),
(35, 'CEPOFION  SERBUK INJEKSI 1 g', 'CEPOFIOSI-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4.67, 2.67, 3.67, 1, 1),
(36, 'CHLODINE HAND RUB 0.5% 5 L', 'CHLO0.5%5L', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5, 4.99, 5, 1, 1),
(37, 'CHLODINE HAND RUB 0.5% 50 ML', 'CHLO0.5%50', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 14, 12, 13, 1, 1),
(38, 'CHLODINE HAND RUB 0.5% 500 ML', 'CHLON0.5%-', '2022-04-06 20:35:52.817071', '2022-07-15 14:19:38.052134', 1, 547, 517, 4, 1, 1),
(39, 'CHLODINE SCRUB 2% 1 L', 'CHLO2PSC1-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 11.3, 9.3, 10.3, 1, 1),
(40, 'CHLODINE SCRUB 2% 5 L', 'CHLO2PSC5-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 6, 4, 5, 1, 1),
(41, 'CHLODINE SCRUB 2% 500 ML', 'CHLO2PSC--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 6, 4, 5, 1, 1),
(42, 'CHLODINE SCRUB 4% 500 ML', 'CHLON4%500', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4.5, 4.45, 4.5, 1, 1),
(43, 'CHLODINE SCRUB 4% 5L', 'CHLON4%5L-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5, 4.99, 5, 1, 1),
(44, 'CHLODINE SWAB', 'CHLODSWAB-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 6.3, 4.3, 5.3, 1, 1),
(45, 'CIPROFLOXACIN HCL MONOHYDRATE TSS 500 MG', 'CIPRO500T-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4, 2, 3, 1, 1),
(46, 'CITICOLINE SODIUM TABLET 500 mg', 'ICITI500--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5.05, 3.05, 4.05, 1, 1),
(47, 'CITION INJEKSI 1000 mg/ 8 ml', 'CTIONI1000', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1, 1, 1, 1),
(48, 'CITION INJEKSI 250 mg/2 ml', 'CITIONI250', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4.2, 2.2, 3.2, 1, 1),
(49, 'CITION KAPLET 1000 mg', 'CTION1000K', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2.85, 0.85, 1.85, 1, 1),
(50, 'CITION TABLET 500 mg', 'CITIONT500', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4.95, 2.95, 3.95, 1, 1),
(51, 'CLOFION TSS 75 MG', 'CLOFION75-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2.9, 0.9, 1.9, 1, 1),
(52, 'CLOPIDOGREL BISULFATE TSS 75 MG', 'ICLPDGRL75', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3, 1, 2, 1, 1),
(53, 'DANSEFION INJEKSI 4 mg/2 ml ', 'DANSEF4IN-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4.5, 2.5, 3.5, 1, 1),
(54, 'DANSEFION KSS 4 MG', 'DANSETAB4-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2.9, 1, 1.9, 1, 1),
(55, 'DANSEFION KSS 8 MG', 'DANSETAB8-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2.9, 1, 1.9, 1, 1),
(56, 'DANSEFION SIRUP 4 MG/5 ML', 'DANSESYR4-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 9.15, 7.15, 8.15, 1, 1),
(57, 'DEXTO INJEKSI 50 MG/2 ML', 'DEXTOI50--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4.3, 2.3, 3.2, 1, 1),
(58, 'DEXTO TABLET SALUT SELAPUT 25 mg', 'DEXTO25---', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4, 3.4, 3.5, 1, 1),
(59, 'DOMPERIDONE MALEATE TABLET SALUT SELAPUT 10 mg', 'IDOMPE----', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3.6, 1.6, 2.6, 1, 1),
(60, 'EASYEF 0.005% 10 ML', 'EASYEF10--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 15, 13, 14, 1, 1),
(61, 'EPODION 10.000 IU', 'EPO10000IU', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 11, 9, 10, 1, 1),
(62, 'EPODION 2000 IU', 'EPO2000IU-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 11, 9, 10, 1, 1),
(63, 'EPODION 3000 IU', 'EPO3000IU-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 11, 9, 10, 1, 1),
(64, 'EPODION 4000 IU', 'EPO4000IU-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 11, 9, 10, 1, 1),
(65, 'ERTIX SIRUP KERING 175 mg/5ml', 'ERTIXSK---', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1, 1, 1, 1),
(66, 'ESOFIN SERBUK INJEKSI 40 MG', 'ESOFION40-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5.5, 3.5, 4.5, 1, 1),
(67, 'ESOMEPRAZOLE SOD. INJ 40 MG', 'IESOME40--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5.5, 3.5, 4.5, 1, 1),
(68, 'ETARFION SERBUK INJEKSI 25 MG', 'ETARFION25', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 16, 14, 15, 1, 1),
(69, 'ETOFION INJEKSI IV/IM 30 mg/ml ', 'ETOFI30I--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3.49, 1.49, 2.49, 1, 1),
(70, 'EVOFION INFUS 500 mg/100 ml', 'EVOF500IF-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 13.12, 11.12, 12.12, 1, 1),
(71, 'EVOFION INFUS 750 MG/150 ML', 'EVOF750IF-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 15, 11, 13, 1, 1),
(72, 'EVOFION TSS 500 MG', 'EVOFTSS500', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1, 1, 1, 1),
(73, 'FERION INJEKSI 100 MG/5 ML', 'FRION100/5', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 6.99, 4.99, 5.99, 1, 1),
(74, 'FERTION TABLET 50 MG', 'FERTIONTAB', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5, 4, 5, 1, 1),
(75, 'FIBUMIN KAPSUL', 'FIBUMIN---', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2.7, 1, 1.67, 1, 1),
(76, 'FIBUMIN PLUS SIRUP 100ML', 'FIPLSYR100', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1, 1, 1, 1),
(77, 'FIBUMIN PLUS SIRUP 60ML', 'FIPLUSYR60', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1, 1, 1, 1),
(78, 'FIOCILAS SERBUK INFUS 1 g ', 'FIOCIL1SI-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5.66, 3.66, 4.66, 1, 1),
(79, 'FIONDAZOL INFUS 500 mg/100 ml', 'FIOND500IF', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 13.12, 11.12, 12.12, 1, 1),
(80, 'FIONTIC SERBUK INJEKSI 1 g', 'FIONTIC1SI', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5.12, 3.12, 4.12, 1, 1),
(81, 'FIONVASK KAPLET 10 MG', 'IFFIONVK10', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3, 1, 2, 1, 1),
(82, 'FIONVASK KAPLET 5 MG', 'IFFIONVSK5', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4, 2, 3, 1, 1),
(83, 'FIOPRAZ SERBUK INJEKSI 40 mg', 'FIOPRZ40SI', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5.97, 3.97, 4.97, 1, 1),
(84, 'FIORAMOL INFUS 1 g/100 ml', 'FIORML1IF-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 13.04, 11.04, 12.04, 1, 1),
(85, 'FIORAMOL SUPPO 160 MG', 'FIORSUP160', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5, 4.9, 5, 1, 1),
(86, 'FIORAMOL SUPPO 80 MG', 'FIORSUPP80', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5, 4.9, 5, 1, 1),
(87, 'FIOTRAM KAPLET SALUT SELAPUT', 'FIOTRAMKSS', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3.04, 1.04, 2.04, 1, 1),
(88, 'FIRONIUM INJEKSI 50 mg/5 ml', 'FRONIUM---', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 6, 4.99, 5, 1, 1),
(89, 'FRIZIN SIRUP 5 MG/5ML', 'FRIZNSR5MG', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 9, 7.1, 8, 1, 1),
(90, 'FRIZIN TABLET SALUT SELAPUT 10 mg', 'FRIZIN10--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1.4, 1.7, 1, 1),
(91, 'GABAFION KAPSUL 300 MG', 'GABFIONK--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3.1, 1.1, 2.1, 1, 1),
(92, 'GABAPENTIN KAPSUL 300 MG', 'IGABA300K-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3.1, 1.1, 2.1, 1, 1),
(93, 'GANION INJEKSI 1 MG/1 ML', 'GANIONI1--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5.5, 3.5, 4.56, 1, 1),
(94, 'GANION INJEKSI 3 MG/3 ML', 'GANIONI3--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5.56, 3.56, 4.56, 1, 1),
(95, 'GETYN INJEKSI 80 MG/2 ML', 'GETYNINJ--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3, 1, 2, 1, 1),
(96, 'GLARITUS INJEKSI 100 IU 3 ML (DISPOPEN)', 'GLAR100IU3', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 16, 14, 15, 1, 1),
(97, 'GLIMEFION TABLET 1 mg', 'GLIMFION1-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4.35, 2.35, 3.35, 1, 1),
(98, 'GLIMEFION TABLET 2 mg', 'GLIMFION2-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4.35, 2.35, 3.35, 1, 1),
(99, 'GLIMEFION TABLET 4 mg', 'GLIMFION4-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4.35, 2.35, 3.35, 1, 1),
(100, 'GLIMEPIRIDE TABLET 1 mg', 'IGLIME1---', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4.65, 2.65, 3.65, 1, 1),
(101, 'GLIMEPIRIDE TABLET 2 mg', 'IGLIME2---', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4.65, 2.65, 3.65, 1, 1),
(102, 'GLIMEPIRIDE TABLET 3 mg', 'IGLIME3---', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4.65, 2.65, 3.65, 1, 1),
(103, 'GLIMEPIRIDE TABLET 4 mg', 'IGLIME4---', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4.65, 2.65, 3.65, 1, 1),
(104, 'GOXO SIRUP 60 ML', 'GOXOSYR---', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 8.5, 8, 8, 1, 1),
(105, 'HANTIZER 5 L', 'HANTIZER5L', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5, 4.9, 5, 1, 1),
(106, 'HANTIZER 500 ML', 'HATIZER500', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4.5, 4.45, 4.5, 1, 1),
(107, 'HENCLIN 2% 1 L', 'HCLIN2%1L-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1, 1, 1, 1),
(108, 'HENCLIN 2% 5 L', 'HCLIN2%5L-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 6, 4, 5, 1, 1),
(109, 'HENCLIN 2% 50 ML', 'HCLIN2%50-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1, 1, 1, 1),
(110, 'HENCLIN 2% 500 ML', 'HCLIN2%500', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 6, 4, 5, 1, 1),
(111, 'HENCLIN 4% 1 L', 'HCLIN4%1L-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1, 1, 1, 1),
(112, 'HENCLIN 4% 5 L', 'HCLIN4%5L-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 6, 4, 5, 1, 1),
(113, 'HENCLIN 4% 50 ML', 'HCLIN4%50-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1, 1, 1, 1),
(114, 'HENCLIN 4% 500 ML', 'HCLIN4%500', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 6, 4, 5, 1, 1),
(115, 'HENCLIN 5 L', 'HENCLIN5L-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 6, 4, 5, 1, 1),
(116, 'HENCLIN 50 ML', 'HENCLIN50-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 14, 12, 13, 1, 1),
(117, 'HENCLIN 500 ML', 'HENCLIN500', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 6, 4, 5, 1, 1),
(118, 'HENCLIN SWAB 0.5%', 'HCLNSWB0.5', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1, 1, 1, 1),
(119, 'HENCLIN SWAB 2%', 'HCLINSWAB-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1, 1, 1, 1),
(120, 'HESFION 130 INFUS', 'HESF130INF', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 11.7, 9.7, 10.7, 1, 1),
(121, 'HUMAN IMMUNOGLOBULIN (pH4) FOR IV', 'HIVIGPH4--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 16, 14, 15, 1, 1),
(122, 'INBACEF KAPLET SALUT SELAPUT 200 mg', 'INBACF200-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4.12, 2.12, 3.12, 1, 1),
(123, 'INBACEF SIRUP KERING 100 mg/5 ml', 'INBACFSK--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 6.41, 4.41, 5.41, 1, 1),
(124, 'INFIBIOTIC SERBUK INJEKSI 1 g', 'INFIBIOTSI', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5.46, 4.86, 5.16, 1, 1),
(125, 'INFIBIOTIC SI 1 G (EXPORT) @ 10', 'INFIBIO10-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5.46, 4.86, 5.16, 1, 1),
(126, 'INFIMOX INFUS IV 400 mg/250 ml', 'INFIMOXINF', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 16.5, 14.5, 15.5, 1, 1),
(127, 'INFIMOX KSS 400 MG', 'INFMX400K-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2.74, 0.74, 1.74, 1, 1),
(128, 'INFIMYCIN KSS 500 MG', 'INFIM500K-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3, 1, 2, 1, 1),
(129, 'INFIMYCIN SERBUK INFUS 0,5 g ', 'INFYMC----', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2.77, 0.77, 1.77, 1, 1),
(130, 'INFIMYCIN SIRUP KERING 200 mg/5 ml', 'INFIMS----', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 9.89, 7.89, 8.89, 1, 1),
(131, 'INFINEM SERBUK INJEKSI 1 g', 'INFINE1SI-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 6.38, 4.38, 5.38, 1, 1),
(132, 'INFITOL INFUS 100 g/500 ml', 'INFITOL100', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 11.7, 9.6, 10.6, 1, 1),
(133, 'INFUXACIN INFUS 200 mg/100 ml', 'INFUXACINF', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 12.97, 10.97, 11.97, 1, 1),
(134, 'INLACYL KAPLET SALUT SELAPUT 500 mg', 'INLAC500K-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 6.3, 4.3, 5.3, 1, 1),
(135, 'INTORVAS KAPLET SALUT SELAPUT 40 mg', 'INTOR40---', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3.04, 1.04, 2.04, 1, 1),
(136, 'INZON SERBUK INJEKSI 1 g', 'INZON1SI--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4.35, 2.35, 3.35, 1, 1),
(137, 'KETOROLAC TROMETAMOL TSS 10 MG', 'KETROLCTSS', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1.7, 1.7, 1, 1),
(138, 'KIDYVIT APPETITE BOOSTER SYRUP 100 ML', 'KIDYVIT100', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 9, 7, 8, 1, 1),
(139, 'KIDYVIT APPETITE BOOSTER TAB KUNYAH', 'KIDAPPTAB-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1, 1, 1, 1),
(140, 'KIDYVIT EMULSION 250 ML', 'KIDVITEMUL', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5, 4, 5, 1, 1),
(141, 'KIDYVIT FRUIT VEGIE SYRUP 100 ML', 'KIDFRVESY-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4.9, 4, 5, 1, 1),
(142, 'KIDYVIT FRUIT VEGIE TABLET KUNYAH ', 'KIDFRVETAB', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5, 4, 5, 1, 1),
(143, 'KIDYVIT GOLD 250 ML', 'KIDYVTGOLD', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5, 4, 5, 1, 1),
(144, 'KIDYVIT JR DROP 10 ML', 'KIDYVITDRP', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1, 10, 1, 1),
(145, 'KIDYVIT SIRUP 60 ML', 'KIDYSYR60-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 8.64, 6.64, 7.64, 1, 1),
(146, 'KIDYVIT SMART SYRUP 100 ML', 'KIDYVISMAR', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5, 4, 5, 1, 1),
(147, 'KOLEFION TABLET SALUT SELAPUT 20 mg', 'KOLEFION20', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1.4, 1.7, 1, 1),
(148, 'LEVOFLOXACIN HEMIHYDRATE TSS 500 MG', 'ILEVTSS500', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 7.5, 5.5, 6.5, 1, 1),
(149, 'LEVOFLOXACIN INFUS 500 mg/100 mL ', 'ILEVO500IF', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 12.96, 10.96, 11.96, 1, 1),
(150, 'LEVOFLOXACIN INFUS 750 mg/150 ml', 'ILEVO750--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 12.76, 10.76, 11.76, 1, 1),
(151, 'MECOBALAMIN INJEKSI 500 MCG/ML', 'MECOINJ---', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4.28, 2.28, 3.51, 1, 1),
(152, 'MEFENAMIC ACID KSS 500 MG', 'IASMEF500K', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5.05, 3.05, 4.05, 1, 1),
(153, 'MELFION TABLET 15 MG', 'MELFION15-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3.64, 1.64, 2.64, 1, 1),
(154, 'MELOXICAM TABLET 15 MG', 'IMLXCMT15-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3.64, 1.64, 2.64, 1, 1),
(155, 'MELOXICAM TABLET 7.5 MG ', 'IMLXCMT7.5', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3.62, 1.62, 2.62, 1, 1),
(156, 'MEROPENEM TRIHYDRATE  SERBUK INJEKSI 1 g', 'MEROP1SI--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4.72, 2.72, 3.72, 1, 1),
(157, 'METHYLPREDNISOLON TABLET 16 mg ', 'IMETHYL16-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1, 1, 1, 1),
(158, 'METHYLPREDNISOLON TABLET 4 mg ', 'IMETHYL4MG', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3.1, 1.1, 2.1, 1, 1),
(159, 'METHYLPREDNISOLON TABLET 8 mg', 'IMETHYL8MG', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3.1, 1.1, 2.1, 1, 1),
(160, 'MOMEFION CREAM 0,1%', 'MOMEFION10', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 7.85, 5.85, 6.85, 1, 1),
(161, 'MOXIFLOXACIN HCL KSS 400 MG', 'IMOXIFL400', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2.74, 0.74, 1.74, 1, 1),
(162, 'MULTI-GYN ACTIGEL 2 ML', 'MULTIGYN2-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5, 3, 0.055, 1, 1),
(163, 'MULTI-GYN ACTIGEL 30 ML', 'MULTIGYN30', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5, 3, 4, 1, 1),
(164, 'MULTI-MAM COMPRESSES ', 'MULTIMAMSH', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5, 3, 4, 1, 1),
(165, 'N-CETYN INHALASI 100 MG/ML', 'NCETYNINH-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4.25, 2.25, 3.25, 1, 1),
(166, 'NICARFION  INJEKSI 10 mg/10 ml', 'NICARFIONI', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5.21, 3.21, 4.21, 1, 1),
(167, 'NORFION INJEKSI 4 mg/4 ml', 'NORFION4--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 6.99, 4.99, 5.99, 1, 1),
(168, 'OCTADIN 0.1 SPRAY 50 ML', 'OCTD50SP--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 14, 12, 13, 1, 1),
(169, 'OCTADIN GEL', 'OCTDGEL---', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4.12, 2.12, 3.12, 1, 1),
(170, 'OCTADIN SC ANTISEPTIK 100 ML', 'OCTDSC100-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5, 4.5, 5, 1, 1),
(171, 'OCTADIN SC ANTISEPTIK 50 ML', 'OCTDSC50--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 14, 11, 13, 1, 1),
(172, 'OCTADIN SOL 0.1 1 L', 'OCTD1L----', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1, 1, 1, 1),
(173, 'OCTADIN SWAB', 'OCTDSWAB--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1, 1, 1, 1),
(174, 'ONDANSETRON HCl DIHIDRATE KSS 4 MG', 'IONDANT4--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2.9, 1, 1.9, 1, 1),
(175, 'ONDANSETRON HCl DIHIDRATE KSS 8 MG', 'IONDANT8--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2.9, 1, 1.9, 1, 1),
(176, 'OSERIN KAPSUL 50 MG', 'OSERINKAP-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1, 1, 1, 1),
(177, 'OSTEOFORTIS KAPSUL', 'OSTEOKAP--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4.9, 2.9, 3.9, 1, 1),
(178, 'PANTOPRAZOLE SODIUM SERBUK INJEKSI 40 MG', 'PANTO40SI-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1, 1, 1, 1),
(179, 'PEDIALON 1.5%', 'PEDIALN1.5', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1, 1, 1, 1),
(180, 'PEDIALON 2.5%', 'PEDIALN2.5', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1, 1, 1, 1),
(181, 'PELARUT SOLFION INJEKSI 125 MG', 'PELTSOL125', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5, 4.5, 5, 1, 1),
(182, 'PHOSBIND KAPLET', 'PHOSBNDKAP', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3, 2.5, 3, 1, 1),
(183, 'PHYFION INJEKSI 2 mg/ml', 'PYFIONINJ-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4.13, 2.13, 3.13, 1, 1),
(184, 'PIROFION SERBUK INJEKSI 1 g', 'PIROF1SI--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4.17, 2.17, 3.17, 1, 1),
(185, 'PUREKAF FLU & COUGH SYRUP 60 ML', 'PUREKAFSYR', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 8.3, 6.3, 7.3, 1, 1),
(186, 'PUREKAF TABLET 8 MG', 'PUREKAF8T-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1, 1, 1, 1),
(187, 'PURVIT D3 @ 60', 'PURVITD360', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3, 1, 2, 1, 1),
(188, 'PURVIT D3 SOFT CAPSUL ', 'PURVITD3--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5, 4, 4, 1, 1),
(189, 'Q-FOLIC FORTE', 'Q-FOLICFOR', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1, 1, 1, 1),
(190, 'Q-FOLIC TSS', 'Q-FOLICTSS', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 11, 9, 10, 1, 1),
(191, 'RANIFIN  INJEKSI 50 mg/2 ml', 'RANIFIN50-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4.25, 2.25, 3.25, 1, 1),
(192, 'RANITIDIN HCl TABLET SALUT SELAPUT 150 mg', 'IRANI150T-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 10.86, 8.86, 9.86, 1, 1),
(193, 'RECALUS KAPSUL @30', 'RECALUS---', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3.1, 1.1, 2.1, 1, 1),
(194, 'REMDESIVIR IV INJEKSI 5 mg/ml', 'REMDESV5--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5, 4.9, 5, 1, 1),
(195, 'REMEVA INJEKSI 100 MG', 'REMEVAINJ-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3.7, 2, 2.7, 1, 1),
(196, 'RENERO INJEKSI @24', 'RENEROINJ-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 6, 5, 5, 1, 1),
(197, 'RENERO INJEKSI @6', 'RENEROINJ6', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3.12, 1.12, 2.12, 1, 1),
(198, 'RESOCAL SERBUK ORAL 5 G', 'RESOCAL---', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1, 1, 1, 1),
(199, 'ROSFION TSS 10 MG', 'ROSFIO10--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3, 2.9, 3, 1, 1),
(200, 'ROSFION TSS 20 mg', 'ROSFION20-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3, 1, 2, 1, 1),
(201, 'ROSUVASTATIN CALCIUM TSS 10 MG', 'IROSUVAS10', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3, 2.9, 2, 1, 1),
(202, 'ROSUVASTATIN CALCIUM TSS 20 MG', 'IROSUVAS20', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3, 1, 2, 1, 1),
(203, 'SIMVASTATIN KAPLET SALUT SELAPUT 20 mg', 'ISIMVAS20-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1.4, 1.7, 1, 1),
(204, 'SOLFION SERBUK INJEKSI 125 MG', 'SOLFSI125-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2.7, 2.5, 2.7, 1, 1),
(205, 'SOLFION TABLET 16 mg', 'SOLFION16T', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1, 1, 1, 1),
(206, 'SOLFION TABLET 4 mg', 'SOLFION4T-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3.1, 1.1, 2.1, 1, 1),
(207, 'SOLFION TABLET 8 mg', 'SOLFION8T-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3.1, 1.1, 2.1, 1, 1),
(208, 'SULPEFION SERBUK INJEKSI 1 g', 'SULPEFISI-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4.44, 2.44, 4.625, 1, 1),
(209, 'SYTIN DROP', 'SYTIND----', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 6.3, 4.3, 5.34, 1, 1),
(210, 'TERMOFEN SUSPENSI 100 mg/5 ml', 'TERMOFENS-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 9.15, 7.15, 8.15, 1, 1),
(211, 'VALACICLOVIR HCl DIHYDRATE KSS 500 mg', 'IVALA500--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 6.25, 4.25, 5.25, 1, 1),
(212, 'VILEON SPRAY 50 ML', 'VILEONSPRY', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1, 1, 1, 1),
(213, 'VITAFION C IM/IV/SC 1G/5ML', 'VITAFIONC-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 6.99, 4.99, 5.99, 1, 1),
(214, 'VOMIPER Drops 5 mg/ml', 'VOMIPD----', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1, 1, 1, 1),
(215, 'VOMIPER SUSPENSI 5 mg/5 ml', 'VOMIPS----', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 8.85, 6.85, 7.85, 1, 1),
(216, 'VOMIPER TABLET SALUT SELAPUT 10 mg', 'VOMIPT----', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3.65, 1.65, 2.65, 1, 1),
(217, 'WIDOXIL KAPSUL 500 mg', 'WIDOX500K-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 8.43, 6.43, 7.43, 1, 1),
(218, 'WIDOXIL SIRUP KERING 125 mg/5 ml', 'WIDOX125--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 7.37, 6.77, 7.07, 1, 1),
(219, 'WIDOXIL SIRUP KERING 250 mg/5 ml ', 'WIDOX250--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 8.45, 6.45, 7.45, 1, 1),
(220, 'XANICLIN HAND SANITIZER 1 L', 'XANICLI1L-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1, 0, 1, 1),
(221, 'XANICLIN HAND SANITIZER 5 L', 'XANICLI5L-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5, 4, 5, 1, 1),
(222, 'XANICLIN HAND SANITIZER 50 ML', 'XANICLIN--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 14, 12, 13, 1, 1),
(223, 'XANICLIN HAND SANITIZER 500 ML', 'XANICLI500', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5, 4, 5, 1, 1),
(224, 'XANICLIN SCRUB 1 L', 'XANISC1L--', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 11.3, 9.3, 10.3, 1, 1),
(225, 'XANICLIN SCRUB 5 L', 'XANISCR5L-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5, 4.9, 5, 1, 1),
(226, 'XANICLIN SCRUB 50 ML', 'XANISC50ML', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 13.3, 11.3, 12.3, 1, 1),
(227, 'XANICLIN SCRUB 500 ML', 'XANISC500-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 5, 4.9, 5, 1, 1),
(228, 'XETSON INJEKSI 5 MG/ML', 'XETZONINJ-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 11, 9, 10, 1, 1),
(229, 'XETSON KAPLET 0.5 mg', 'XETZONKAP-', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 3, 2, 2.8, 1, 1),
(230, 'YES C KSS 500 MG', 'YESCKSS500', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 4.9, 2.9, 3.9, 1, 1),
(231, 'ZILMASK 3 PLY MASKER EARLOOP', 'ZILMSK-EAR', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1, 1, 1, 1),
(232, 'ZILMASK 3 PLY MASKER HEADLOOP', 'ZILMSKHEAD', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 2, 1, 1, 1, 1),
(233, 'ZINFION SIRUP 20 MG/5 ML', 'ZINFION---', '2022-04-06 20:35:52.817071', '2022-04-06 20:35:52.817071', 1, 8.5, 8, 8, 1, 1),
(234, 'ALKOHOL 70 %', 'ALK70L', '2022-06-17 11:06:55.547187', '2022-06-17 11:06:55.547230', 1, 4, 2, 3, 1, NULL),
(235, 'ALKOHOL 50 %', 'ALK50', '2022-06-21 08:35:08.741172', '2022-06-21 08:35:23.497463', 0, 5, 3, 4, 1, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `mainApp_register`
--

CREATE TABLE `mainApp_register` (
  `id` int NOT NULL,
  `batchno` varchar(15) NOT NULL,
  `boxno` int NOT NULL,
  `status` int DEFAULT NULL,
  `createdon` datetime(6) NOT NULL,
  `updatedon` datetime(6) NOT NULL,
  `weight` double DEFAULT NULL,
  `createdby_id` int NOT NULL,
  `updatedby_id` int DEFAULT NULL,
  `product_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mainApp_register`
--

INSERT INTO `mainApp_register` (`id`, `batchno`, `boxno`, `status`, `createdon`, `updatedon`, `weight`, `createdby_id`, `updatedby_id`, `product_id`) VALUES
(12, 'TESTQR', 4, 1, '2022-04-06 13:33:04.815014', '2022-04-06 13:33:05.503080', 713860, 1, NULL, 38),
(13, 'ITPE04451', 120, 2, '2022-06-01 04:48:56.653786', '2022-06-03 08:14:27.050986', 5374, 1, NULL, 38),
(16, 'ICLG19050', 2, 1, '2022-06-07 02:57:19.460070', '2022-06-07 02:57:21.903738', 5691, 1, NULL, 38),
(17, 'ICLG19050', 6, 1, '2022-06-07 02:58:15.532683', '2022-06-07 02:58:16.914831', 5691, 1, NULL, 38),
(18, 'ICLG19050', 7, 2, '2022-06-07 03:09:59.847481', '2022-06-07 03:10:03.637362', 1534.5, 1, NULL, 38),
(19, 'ICLG19050', 8, 2, '2022-06-07 03:10:20.365029', '2022-06-07 03:10:23.639367', 1534.5, 1, NULL, 38),
(23, 'ICLG19050', 3, 1, '2022-06-07 10:45:24.957083', '2022-06-07 10:46:38.355950', 1550, 1, NULL, 38),
(24, 'ICLG19050', 12, 1, '2022-06-07 10:47:15.431405', '2022-06-07 04:00:21.672910', 5375, 1, NULL, 38),
(27, 'ICLG19050', 4, 1, '2022-06-07 04:35:32.193692', '2022-06-07 04:35:35.577721', 5691, 1, NULL, 38),
(31, 'ICLG19050', 1, 1, '2022-07-14 09:16:00.188194', '2022-07-14 09:21:04.121396', 5000, 1, NULL, 38),
(32, 'ICLG19050', 2, 2, '2022-07-14 09:44:00.920168', '2022-07-14 09:44:37.178683', 7000, 1, NULL, 38),
(33, 'ICLG19050', 1, 0, '2022-07-14 09:45:47.681692', '2022-07-14 09:46:17.417398', 8000, 1, NULL, 38),
(34, 'ICLG19050', 1, 2, '2022-07-14 09:56:21.062474', '2022-07-14 09:56:49.114615', 2000, 1, NULL, 38),
(35, '800', 1, 1, '2022-07-14 10:00:48.133283', '2022-07-14 10:05:11.762143', 3000, 1, NULL, 38),
(36, '800', 2, 0, '2022-07-14 10:10:58.867063', '2022-07-14 10:11:40.113233', 8000, 1, NULL, 38),
(37, 'ICLG19050', 1, 3, '2022-07-14 10:36:00.046451', '2022-07-14 10:36:50.981175', 3000, 1, NULL, 38),
(38, 'ICLG19050', 15, 1, '2022-07-14 12:42:02.521098', '2022-07-14 14:35:12.312711', 450, 1, NULL, 38),
(39, 'ICLG19050', 1, 2, '2022-07-14 15:42:19.023270', '2022-07-14 15:42:48.793134', 5000, 6, NULL, 38),
(40, 'ICLG19050', 1, 1, '2022-07-15 11:43:00.344215', '2022-07-15 13:05:12.716231', 532.7, 1, NULL, 38),
(41, 'ICLG19050', 1, 3, '2022-07-15 13:07:08.879982', '2022-07-15 13:09:48.330087', 532.7, 6, NULL, 38),
(42, 'ICLG19050', 20, 1, '2022-07-15 13:10:39.597741', '2022-07-15 13:10:55.515176', 532.7, 6, NULL, 38),
(43, 'ICLG19050', 21, 2, '2022-07-15 13:11:43.542615', '2022-07-15 13:12:14.740386', 532.7, 6, NULL, 38),
(44, 'ICLG19050', 31, 1, '2022-07-15 13:13:13.500001', '2022-07-15 13:13:22.231079', 532.7, 6, NULL, 38),
(45, 'ICLG19050', 22, 1, '2022-07-15 13:14:16.350372', '2022-07-15 13:14:29.637076', 532.7, 6, NULL, 38),
(46, 'ICLG19050', 56, 1, '2022-07-15 13:22:20.868682', '2022-07-15 13:22:24.661814', 532.5, 6, NULL, 38),
(47, 'ICLG19050', 56, 2, '2022-07-15 13:22:37.879640', '2022-07-15 13:23:09.648504', 532, 6, NULL, 38),
(48, 'ICLG19050', 56, 3, '2022-07-15 13:23:24.741675', '2022-07-15 13:24:31.285937', 532.4, 6, NULL, 38),
(49, 'TEST140722', 2, 3, '2022-07-15 14:09:31.144718', '2022-07-15 14:32:24.821748', 736, 1, NULL, 3),
(50, 'TEST140722', 1, 1, '2022-07-15 14:32:47.930836', '2022-07-15 14:32:59.822525', 532.4, 1, NULL, 3),
(51, 'TEST140722', 3, 1, '2022-07-15 14:33:49.928027', '2022-07-15 14:34:04.801781', 532.4, 1, NULL, 3),
(52, 'TEST140722', 4, 2, '2022-07-15 14:34:08.910762', '2022-07-15 14:34:14.815493', 735.9, 1, NULL, 3),
(53, 'TEST140722', 7, 1, '2022-07-15 14:48:24.068066', '2022-07-15 14:48:37.543258', 532.2, 1, NULL, 3),
(54, 'ICLG19050', 41, 1, '2022-07-15 14:51:12.025642', '2022-07-15 14:51:29.864178', 532.2, 1, NULL, 38),
(55, 'TEST140722', 5, 1, '2022-07-15 15:10:34.332835', '2022-07-15 15:11:09.936089', 735.9, 1, NULL, 3),
(56, 'TEST140722', 6, 3, '2022-07-15 15:11:38.573171', '2022-07-15 15:12:17.526790', 1145.4, 1, NULL, 3),
(57, 'TEST140722', 7, 2, '2022-07-15 15:12:50.569689', '2022-07-15 15:12:59.928867', 1145.4, 1, NULL, 3);

-- --------------------------------------------------------

--
-- Table structure for table `mainApp_report`
--

CREATE TABLE `mainApp_report` (
  `id` int NOT NULL,
  `batchno` varchar(15) NOT NULL,
  `reviewdate` datetime(6) DEFAULT NULL,
  `effectivedate` datetime(6) DEFAULT NULL,
  `dnno` varchar(20) DEFAULT NULL,
  `dnrev` int NOT NULL,
  `createdon` datetime(6) NOT NULL,
  `updatedon` datetime(6) NOT NULL,
  `department_id` int NOT NULL,
  `product_id` int NOT NULL,
  `reporttitle_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mainApp_report`
--

INSERT INTO `mainApp_report` (`id`, `batchno`, `reviewdate`, `effectivedate`, `dnno`, `dnrev`, `createdon`, `updatedon`, `department_id`, `product_id`, `reporttitle_id`) VALUES
(5, 'ICLG19050', '2022-04-01 00:00:00.000000', '2022-04-01 00:00:00.000000', 'ABASDAS123', 1, '2022-04-01 09:34:12.323941', '2022-04-01 09:34:12.323966', 1, 38, 1),
(6, 'ICLG19050', '2022-04-01 00:00:00.000000', '2022-04-01 00:00:00.000000', 'ABASDAS123', 2, '2022-04-02 02:41:45.866424', '2022-04-02 02:41:45.866452', 1, 38, 1),
(7, 'random', '2022-04-06 00:00:00.000000', '2022-04-06 00:00:00.000000', NULL, 7, '2022-04-06 03:04:49.411339', '2022-04-06 03:04:49.411485', 1, 14, 1);

-- --------------------------------------------------------

--
-- Table structure for table `mainApp_reportregister`
--

CREATE TABLE `mainApp_reportregister` (
  `id` int NOT NULL,
  `dnrev` int NOT NULL,
  `batchno` varchar(15) NOT NULL,
  `boxno` int NOT NULL,
  `status` int DEFAULT NULL,
  `createdon` datetime(6) NOT NULL,
  `weight` double DEFAULT NULL,
  `createdby_id` int NOT NULL,
  `product_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `mainApp_reporttitle`
--

CREATE TABLE `mainApp_reporttitle` (
  `id` int NOT NULL,
  `title` varchar(100) NOT NULL,
  `subtitle` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mainApp_reporttitle`
--

INSERT INTO `mainApp_reporttitle` (`id`, `title`, `subtitle`) VALUES
(1, 'WEIGHING RECORD OF PACKING RESULT', 'BUKTI PENIMBANGAN HASIL PENGEMASAN'),
(2, 'WAREHOUSE REPORT', 'LAPORAN GUDANG');

-- --------------------------------------------------------

--
-- Table structure for table `mainApp_uploadedregister`
--

CREATE TABLE `mainApp_uploadedregister` (
  `id` int NOT NULL,
  `batchno` varchar(15) NOT NULL,
  `boxno` int NOT NULL,
  `weight` double NOT NULL,
  `createdon` datetime(6) NOT NULL,
  `updatedon` datetime(6) NOT NULL,
  `product_id` int NOT NULL,
  `measuredate` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `mainApp_weighingstate`
--

CREATE TABLE `mainApp_weighingstate` (
  `id` int NOT NULL,
  `createdon` datetime(6) NOT NULL,
  `updatedon` datetime(6) NOT NULL,
  `product_id` int NOT NULL,
  `status` tinyint(1) NOT NULL,
  `batchno` varchar(15) NOT NULL,
  `spvgudang_id` int DEFAULT NULL,
  `spvpabrik_id` int DEFAULT NULL,
  `pendingstatus` tinyint(1) NOT NULL,
  `operator_id` int DEFAULT NULL,
  `petugasgudang_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mainApp_weighingstate`
--

INSERT INTO `mainApp_weighingstate` (`id`, `createdon`, `updatedon`, `product_id`, `status`, `batchno`, `spvgudang_id`, `spvpabrik_id`, `pendingstatus`, `operator_id`, `petugasgudang_id`) VALUES
(1, '2022-06-01 03:19:18.622958', '2022-06-01 03:19:18.623000', 158, 0, 'ITPE04451', NULL, NULL, 1, NULL, NULL),
(2, '2022-06-07 02:03:12.405091', '2022-06-07 02:03:12.405131', 38, 0, 'ICLG19050', NULL, NULL, 1, NULL, NULL),
(3, '2022-06-09 07:36:11.587997', '2022-06-09 07:36:11.588036', 158, 0, 'ITPN00147', NULL, NULL, 1, NULL, NULL),
(4, '2022-06-15 05:21:29.568375', '2022-06-15 05:21:29.568582', 5, 0, 'COBA2', NULL, NULL, 1, NULL, NULL),
(5, '2022-06-15 05:29:45.621466', '2022-06-15 05:29:45.621624', 5, 0, '78940', NULL, NULL, 1, NULL, NULL),
(6, '2022-06-21 08:52:20.835681', '2022-06-21 08:52:20.835967', 1, 0, 'PROD765', NULL, NULL, 1, NULL, NULL),
(7, '2022-06-21 08:56:59.052867', '2022-06-21 08:56:59.053123', 7, 0, 'SPVGDG01', NULL, NULL, 1, NULL, NULL),
(8, '2022-07-05 14:16:45.963196', '2022-07-05 14:16:45.963244', 13, 0, 'TEST90', NULL, NULL, 1, NULL, NULL),
(10, '2022-07-05 16:07:18.580461', '2022-07-05 16:07:18.580509', 1, 0, 'SPVGDG1', NULL, NULL, 1, NULL, NULL),
(11, '2022-07-13 16:47:10.193651', '2022-07-13 16:47:10.193697', 4, 0, '567', NULL, NULL, 1, NULL, NULL),
(12, '2022-07-14 09:26:23.145603', '2022-07-14 09:26:23.145648', 36, 0, '900', NULL, NULL, 1, NULL, NULL),
(13, '2022-07-14 09:31:37.305552', '2022-07-14 09:31:37.305599', 38, 0, '800', NULL, NULL, 1, NULL, NULL),
(14, '2022-07-14 11:19:27.972961', '2022-07-14 11:19:27.973010', 3, 1, 'TEST140722', NULL, NULL, 1, NULL, NULL),
(15, '2022-07-14 11:21:33.754977', '2022-07-14 11:21:33.755022', 38, 0, 'TESTQR', NULL, NULL, 1, NULL, NULL),
(16, '2022-07-14 15:01:10.812565', '2022-07-14 15:01:10.812613', 1, 0, 'TESTSPVGDG', NULL, NULL, 1, NULL, NULL),
(17, '2022-07-14 15:15:18.268163', '2022-07-14 15:15:18.268212', 1, 0, 'SPVPRD321', NULL, NULL, 1, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `secureapp_accesslist`
--

CREATE TABLE `secureapp_accesslist` (
  `id` int NOT NULL,
  `feature_alias` varchar(30) NOT NULL,
  `feature_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `secureapp_accesslist`
--

INSERT INTO `secureapp_accesslist` (`id`, `feature_alias`, `feature_name`) VALUES
(1, 'home', 'Home'),
(2, 'simulator', 'Simulator'),
(3, 'masterproduct', 'Master Product'),
(4, 'masterdepartment', 'Master Department'),
(5, 'masterreport', 'Master Report'),
(6, 'history', 'History'),
(7, 'reportcsv', 'Report CSV'),
(8, 'reportpdf', 'Report PDF'),
(9, 'managebatch', 'Manage Batch'),
(10, 'viewendbatch', 'View and End Batch');

-- --------------------------------------------------------

--
-- Table structure for table `secureapp_accesslist_allowed_groups`
--

CREATE TABLE `secureapp_accesslist_allowed_groups` (
  `id` int NOT NULL,
  `accesslist_id` int NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `secureapp_accesslist_allowed_groups`
--

INSERT INTO `secureapp_accesslist_allowed_groups` (`id`, `accesslist_id`, `group_id`) VALUES
(32, 1, 1),
(33, 1, 2),
(17, 1, 3),
(18, 1, 4),
(3, 1, 5),
(16, 1, 6),
(19, 1, 7),
(34, 2, 3),
(35, 3, 3),
(36, 3, 4),
(20, 3, 7),
(37, 4, 3),
(38, 4, 4),
(21, 4, 7),
(39, 5, 3),
(40, 5, 4),
(22, 5, 7),
(41, 6, 1),
(42, 6, 2),
(43, 6, 3),
(24, 6, 6),
(25, 7, 3),
(27, 7, 6),
(28, 7, 7),
(51, 8, 1),
(46, 8, 2),
(47, 8, 3),
(52, 8, 5),
(48, 9, 2),
(49, 9, 3),
(57, 10, 1),
(54, 10, 2),
(55, 10, 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `Logging`
--
ALTER TABLE `Logging`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `mainApp_department`
--
ALTER TABLE `mainApp_department`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `mainApp_printheader`
--
ALTER TABLE `mainApp_printheader`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `mainApp_product`
--
ALTER TABLE `mainApp_product`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `code` (`code`),
  ADD KEY `mainApp_product_createdby_id_e42b810b_fk_auth_user_id` (`createdby_id`),
  ADD KEY `mainApp_product_updatedby_id_5f1f19c7_fk_auth_user_id` (`updatedby_id`);

--
-- Indexes for table `mainApp_register`
--
ALTER TABLE `mainApp_register`
  ADD PRIMARY KEY (`id`),
  ADD KEY `mainApp_register_createdby_id_191865be_fk_auth_user_id` (`createdby_id`),
  ADD KEY `mainApp_register_updatedby_id_82d99d62_fk_auth_user_id` (`updatedby_id`),
  ADD KEY `mainApp_register_product_id_f2084192_fk_mainApp_product_id` (`product_id`);

--
-- Indexes for table `mainApp_report`
--
ALTER TABLE `mainApp_report`
  ADD PRIMARY KEY (`id`),
  ADD KEY `mainApp_report_department_id_c477140b_fk_mainApp_department_id` (`department_id`),
  ADD KEY `mainApp_report_product_id_62402e64_fk_mainApp_product_id` (`product_id`),
  ADD KEY `mainApp_report_reporttitle_id_2a284943_fk_mainApp_reporttitle_id` (`reporttitle_id`);

--
-- Indexes for table `mainApp_reportregister`
--
ALTER TABLE `mainApp_reportregister`
  ADD PRIMARY KEY (`id`),
  ADD KEY `mainApp_reportregister_createdby_id_9da5d4d7_fk_auth_user_id` (`createdby_id`),
  ADD KEY `mainApp_reportregister_product_id_7222bfd9_fk_mainApp_product_id` (`product_id`);

--
-- Indexes for table `mainApp_reporttitle`
--
ALTER TABLE `mainApp_reporttitle`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `mainApp_uploadedregister`
--
ALTER TABLE `mainApp_uploadedregister`
  ADD PRIMARY KEY (`id`),
  ADD KEY `mainApp_uploadedregi_product_id_2ab6e08b_fk_mainApp_p` (`product_id`);

--
-- Indexes for table `mainApp_weighingstate`
--
ALTER TABLE `mainApp_weighingstate`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `mainApp_weighingstate_batchno_22e60813_uniq` (`batchno`),
  ADD KEY `mainApp_productstate_product_id_c61ff09f_fk_mainApp_product_id` (`product_id`),
  ADD KEY `mainApp_weighingstate_spvgudang_id_c632282d_fk_auth_user_id` (`spvgudang_id`),
  ADD KEY `mainApp_weighingstate_spvpabrik_id_1fe63769_fk_auth_user_id` (`spvpabrik_id`),
  ADD KEY `mainApp_weighingstate_operator_id_38c46aaf_fk_auth_user_id` (`operator_id`),
  ADD KEY `mainApp_weighingstate_petugasgudang_id_7b8d61ec_fk_auth_user_id` (`petugasgudang_id`);

--
-- Indexes for table `secureapp_accesslist`
--
ALTER TABLE `secureapp_accesslist`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `feature_alias` (`feature_alias`);

--
-- Indexes for table `secureapp_accesslist_allowed_groups`
--
ALTER TABLE `secureapp_accesslist_allowed_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `secureapp_accesslist_all_accesslist_id_group_id_62071da9_uniq` (`accesslist_id`,`group_id`),
  ADD KEY `secureapp_accesslist_group_id_00a025d3_fk_auth_grou` (`group_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=73;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- AUTO_INCREMENT for table `Logging`
--
ALTER TABLE `Logging`
  MODIFY `Id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1084127;

--
-- AUTO_INCREMENT for table `mainApp_department`
--
ALTER TABLE `mainApp_department`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `mainApp_printheader`
--
ALTER TABLE `mainApp_printheader`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `mainApp_product`
--
ALTER TABLE `mainApp_product`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=236;

--
-- AUTO_INCREMENT for table `mainApp_register`
--
ALTER TABLE `mainApp_register`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=58;

--
-- AUTO_INCREMENT for table `mainApp_report`
--
ALTER TABLE `mainApp_report`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `mainApp_reportregister`
--
ALTER TABLE `mainApp_reportregister`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `mainApp_reporttitle`
--
ALTER TABLE `mainApp_reporttitle`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `mainApp_uploadedregister`
--
ALTER TABLE `mainApp_uploadedregister`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `mainApp_weighingstate`
--
ALTER TABLE `mainApp_weighingstate`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `secureapp_accesslist`
--
ALTER TABLE `secureapp_accesslist`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `secureapp_accesslist_allowed_groups`
--
ALTER TABLE `secureapp_accesslist_allowed_groups`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=58;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `mainApp_product`
--
ALTER TABLE `mainApp_product`
  ADD CONSTRAINT `mainApp_product_createdby_id_e42b810b_fk_auth_user_id` FOREIGN KEY (`createdby_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `mainApp_product_updatedby_id_5f1f19c7_fk_auth_user_id` FOREIGN KEY (`updatedby_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `mainApp_register`
--
ALTER TABLE `mainApp_register`
  ADD CONSTRAINT `mainApp_register_createdby_id_191865be_fk_auth_user_id` FOREIGN KEY (`createdby_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `mainApp_register_product_id_f2084192_fk_mainApp_product_id` FOREIGN KEY (`product_id`) REFERENCES `mainApp_product` (`id`),
  ADD CONSTRAINT `mainApp_register_updatedby_id_82d99d62_fk_auth_user_id` FOREIGN KEY (`updatedby_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `mainApp_report`
--
ALTER TABLE `mainApp_report`
  ADD CONSTRAINT `mainApp_report_department_id_c477140b_fk_mainApp_department_id` FOREIGN KEY (`department_id`) REFERENCES `mainApp_department` (`id`),
  ADD CONSTRAINT `mainApp_report_product_id_62402e64_fk_mainApp_product_id` FOREIGN KEY (`product_id`) REFERENCES `mainApp_product` (`id`),
  ADD CONSTRAINT `mainApp_report_reporttitle_id_2a284943_fk_mainApp_reporttitle_id` FOREIGN KEY (`reporttitle_id`) REFERENCES `mainApp_reporttitle` (`id`);

--
-- Constraints for table `mainApp_reportregister`
--
ALTER TABLE `mainApp_reportregister`
  ADD CONSTRAINT `mainApp_reportregister_createdby_id_9da5d4d7_fk_auth_user_id` FOREIGN KEY (`createdby_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `mainApp_reportregister_product_id_7222bfd9_fk_mainApp_product_id` FOREIGN KEY (`product_id`) REFERENCES `mainApp_product` (`id`);

--
-- Constraints for table `mainApp_uploadedregister`
--
ALTER TABLE `mainApp_uploadedregister`
  ADD CONSTRAINT `mainApp_uploadedregi_product_id_2ab6e08b_fk_mainApp_p` FOREIGN KEY (`product_id`) REFERENCES `mainApp_product` (`id`);

--
-- Constraints for table `mainApp_weighingstate`
--
ALTER TABLE `mainApp_weighingstate`
  ADD CONSTRAINT `mainApp_productstate_product_id_c61ff09f_fk_mainApp_product_id` FOREIGN KEY (`product_id`) REFERENCES `mainApp_product` (`id`),
  ADD CONSTRAINT `mainApp_weighingstate_operator_id_38c46aaf_fk_auth_user_id` FOREIGN KEY (`operator_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `mainApp_weighingstate_petugasgudang_id_7b8d61ec_fk_auth_user_id` FOREIGN KEY (`petugasgudang_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `mainApp_weighingstate_spvgudang_id_c632282d_fk_auth_user_id` FOREIGN KEY (`spvgudang_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `mainApp_weighingstate_spvpabrik_id_1fe63769_fk_auth_user_id` FOREIGN KEY (`spvpabrik_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `secureapp_accesslist_allowed_groups`
--
ALTER TABLE `secureapp_accesslist_allowed_groups`
  ADD CONSTRAINT `secureapp_accesslist_accesslist_id_4e67f97e_fk_secureapp` FOREIGN KEY (`accesslist_id`) REFERENCES `secureapp_accesslist` (`id`),
  ADD CONSTRAINT `secureapp_accesslist_group_id_00a025d3_fk_auth_grou` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
