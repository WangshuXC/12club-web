/*
 Navicat Premium Data Transfer

 Source Server         : 1
 Source Server Type    : MySQL
 Source Server Version : 80012 (8.0.12)
 Source Host           : localhost:3306
 Source Schema         : 12club

 Target Server Type    : MySQL
 Target Server Version : 80012 (8.0.12)
 File Encoding         : 65001

 Date: 26/03/2024 18:33:34
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for anime
-- ----------------------------
DROP TABLE IF EXISTS `anime`;
CREATE TABLE `anime`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `episode_count` int(11) NOT NULL DEFAULT 12,
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `title_another` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `title_japanese` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `description` varchar(4095) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `isover` tinyint(1) NOT NULL DEFAULT 0,
  `release_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `view_count` int(11) NOT NULL DEFAULT 0,
  `download_count` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 58 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of anime
-- ----------------------------
INSERT INTO `anime` VALUES (1, 13, '我心里危险的东西', NULL, NULL, '市川京太郎热爱阅读杀人相关的猎奇读物，是个重度的中二病患者。他每天偷看同班的漂亮女生山田杏奈，并且对她作着一些糟糕的幻想。\r\n有一天，山田来到了市川的圣域——图书室。以为四下无人的她，开始大口大口的吃着饭团，还开心地哼着歌。她的这些如此无法预测的行为，让市川的视线，再也无法离开她。', 0, '2024-02-05 07:20:37', '2024-02-12 01:37:51', 8255, 2629);
INSERT INTO `anime` VALUES (2, 12, '我心里危险的东西 第二季', NULL, NULL, NULL, 0, '2024-02-05 07:57:42', '2024-02-11 23:55:16', 4356, 3646);
INSERT INTO `anime` VALUES (3, 12, '药屋少女的呢喃', NULL, NULL, NULL, 0, '2024-02-05 13:37:00', '2024-02-11 23:55:17', 7798, 4193);
INSERT INTO `anime` VALUES (4, 12, '鬼灭之刃', NULL, NULL, NULL, 0, '2024-02-02 17:37:15', '2024-02-11 23:55:18', 2835, 1522);
INSERT INTO `anime` VALUES (5, 12, '鬼灭之刃 无限列车篇', NULL, NULL, NULL, 0, '2024-02-05 20:43:31', '2024-02-11 23:55:19', 663, 4425);
INSERT INTO `anime` VALUES (6, 12, '鬼灭之刃 游郭篇', NULL, NULL, NULL, 0, '2024-01-28 16:26:01', '2024-02-11 23:55:20', 4414, 4041);
INSERT INTO `anime` VALUES (7, 12, '鬼灭之刃 刀匠村篇', NULL, NULL, NULL, 0, '2024-02-06 09:37:33', '2024-02-11 23:55:22', 5922, 1663);
INSERT INTO `anime` VALUES (8, 12, '咒术回战', NULL, NULL, NULL, 0, '2024-01-27 23:48:14', '2024-02-11 23:55:23', 9313, 1341);
INSERT INTO `anime` VALUES (9, 12, '咒术回战 第二季', NULL, NULL, NULL, 0, '2024-01-29 03:35:02', '2024-02-11 23:55:24', 2262, 2269);
INSERT INTO `anime` VALUES (10, 12, '间谍过家家', NULL, NULL, NULL, 0, '2024-02-05 08:46:56', '2024-02-11 23:55:25', 4501, 2546);
INSERT INTO `anime` VALUES (11, 12, '间谍过家家 第二季', NULL, NULL, NULL, 0, '2024-02-03 15:34:17', '2024-02-11 23:55:26', 2231, 3949);
INSERT INTO `anime` VALUES (12, 12, '关于我转生变成史莱姆这档事', NULL, NULL, NULL, 0, '2024-02-04 18:09:58', '2024-02-11 23:55:27', 9654, 500);
INSERT INTO `anime` VALUES (13, 12, '关于我转生变成史莱姆这档事 第二季', NULL, NULL, NULL, 0, '2024-02-05 00:14:05', '2024-02-11 23:55:27', 676, 4433);
INSERT INTO `anime` VALUES (14, 12, '紫罗兰永恒花园', NULL, NULL, NULL, 0, '2024-02-02 07:05:50', '2024-02-11 23:55:28', 9776, 1694);
INSERT INTO `anime` VALUES (15, 12, '小林家的龙女仆', NULL, NULL, NULL, 0, '2024-02-03 04:20:01', '2024-02-11 23:55:30', 9965, 1889);
INSERT INTO `anime` VALUES (16, 12, '小林家的龙女仆 第二季', NULL, NULL, NULL, 0, '2024-02-04 15:16:49', '2024-02-11 23:55:31', 2812, 847);
INSERT INTO `anime` VALUES (17, 12, 'Re：从零开始的异世界生活', NULL, NULL, NULL, 0, '2024-02-03 03:30:47', '2024-02-11 23:55:31', 4234, 2230);
INSERT INTO `anime` VALUES (18, 12, 'Re：从零开始的异世界生活 第二季', NULL, NULL, NULL, 0, '2024-01-31 12:52:37', '2024-02-11 23:55:32', 6444, 439);
INSERT INTO `anime` VALUES (19, 12, '工作细胞', NULL, NULL, NULL, 0, '2024-01-29 11:34:33', '2024-02-11 23:55:33', 8801, 2943);
INSERT INTO `anime` VALUES (20, 12, '工作细胞 第二季', NULL, NULL, NULL, 0, '2024-02-05 01:30:32', '2024-02-11 23:55:33', 4984, 4347);
INSERT INTO `anime` VALUES (21, 12, '冰菓', NULL, NULL, NULL, 0, '2024-02-01 03:35:08', '2024-02-11 23:55:34', 2651, 3669);
INSERT INTO `anime` VALUES (22, 12, '青春猪头少年不会梦到兔女郎学姐', NULL, NULL, NULL, 0, '2024-02-03 22:10:02', '2024-02-11 23:55:35', 7023, 3584);
INSERT INTO `anime` VALUES (23, 12, '埃罗芒阿老师', NULL, NULL, NULL, 0, '2024-02-04 17:20:50', '2024-02-11 23:55:35', 81, 2788);
INSERT INTO `anime` VALUES (24, 12, '欢迎来到实力至上主义的教室', NULL, NULL, NULL, 0, '2024-02-02 18:43:31', '2024-02-11 23:55:40', 6456, 1903);
INSERT INTO `anime` VALUES (25, 12, '四月是你的谎言', NULL, NULL, NULL, 0, '2024-02-01 06:32:01', '2024-02-11 23:55:37', 4218, 843);
INSERT INTO `anime` VALUES (26, 12, '转生成蜘蛛又怎样', NULL, NULL, NULL, 0, '2024-01-29 15:07:12', '2024-02-11 23:55:43', 2878, 1918);
INSERT INTO `anime` VALUES (27, 12, '盾之勇者成名录', NULL, NULL, NULL, 0, '2024-01-27 15:44:41', '2024-02-11 23:55:44', 3663, 237);
INSERT INTO `anime` VALUES (28, 12, '盾之勇者成名录 第二季', NULL, NULL, NULL, 0, '2024-02-05 19:08:45', '2024-02-11 23:55:45', 6144, 2704);
INSERT INTO `anime` VALUES (29, 12, '盾之勇者成名录 第三季', NULL, NULL, NULL, 0, '2024-02-06 04:32:40', '2024-02-11 23:55:46', 6717, 3620);
INSERT INTO `anime` VALUES (30, 12, '在下坂本，有何贵干？', NULL, NULL, NULL, 0, '2024-02-05 11:13:58', '2024-02-11 23:55:46', 5496, 4631);
INSERT INTO `anime` VALUES (31, 12, '中二病也要谈恋爱！', NULL, NULL, NULL, 0, '2024-02-05 18:01:29', '2024-02-11 23:55:47', 1141, 3682);
INSERT INTO `anime` VALUES (32, 12, '约会大作战', NULL, NULL, NULL, 0, '2024-01-28 02:28:53', '2024-02-11 23:55:48', 2154, 1152);
INSERT INTO `anime` VALUES (33, 12, '约会大作战 第二季', NULL, NULL, NULL, 0, '2024-01-31 23:58:33', '2024-02-11 23:55:50', 6428, 1341);
INSERT INTO `anime` VALUES (34, 12, '约会大作战 第三季', NULL, NULL, NULL, 0, '2024-01-29 12:43:29', '2024-02-11 23:55:50', 5884, 97);
INSERT INTO `anime` VALUES (35, 12, '约会大作战 第四季', NULL, NULL, NULL, 0, '2024-02-01 08:15:28', '2024-02-11 23:55:51', 679, 3954);
INSERT INTO `anime` VALUES (36, 12, '总之就是非常可爱', NULL, NULL, NULL, 0, '2024-02-04 21:39:31', '2024-02-11 23:55:53', 8947, 1202);
INSERT INTO `anime` VALUES (37, 0, '总之就是非常可爱 第二季', NULL, NULL, NULL, 0, '2024-01-29 00:45:47', '2024-02-06 15:22:38', 8664, 85);
INSERT INTO `anime` VALUES (38, 0, '我的青春恋爱物语果然有问题', NULL, NULL, NULL, 0, '2024-02-03 13:18:51', '2024-02-06 15:22:38', 7960, 4227);
INSERT INTO `anime` VALUES (39, 0, '路人女主的养成方法', NULL, NULL, NULL, 0, '2024-02-05 22:11:21', '2024-02-06 15:22:38', 7859, 3679);
INSERT INTO `anime` VALUES (40, 0, '五等分的新娘', NULL, NULL, NULL, 0, '2024-02-05 06:46:12', '2024-02-06 15:22:38', 9611, 3946);
INSERT INTO `anime` VALUES (41, 0, '夏日重现', NULL, NULL, NULL, 0, '2024-02-06 07:33:18', '2024-02-06 15:22:38', 192, 1827);
INSERT INTO `anime` VALUES (44, 5, 'Mygo', '', '', '111', 0, '2024-03-21 00:09:30', '2024-03-21 00:09:30', 0, 0);

-- ----------------------------
-- Table structure for anime_comment
-- ----------------------------
DROP TABLE IF EXISTS `anime_comment`;
CREATE TABLE `anime_comment`  (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `anime_id` int(11) NOT NULL,
  `username` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  `ip` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `create_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `content` varchar(4095) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `id`(`id` ASC) USING BTREE,
  INDEX `comment_anime`(`anime_id` ASC) USING BTREE,
  CONSTRAINT `comment_anime` FOREIGN KEY (`anime_id`) REFERENCES `anime` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of anime_comment
-- ----------------------------

-- ----------------------------
-- Table structure for music
-- ----------------------------
DROP TABLE IF EXISTS `music`;
CREATE TABLE `music`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of music
-- ----------------------------

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET macce COLLATE macce_general_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, '1', 'scrypt:32768:8:1$eLiSB0A5LEGIQRkf$afb00778564065efefeb4fb85852b5fddec6873974713b44d169c55a2e0d17d792be0f5a4f335ad94fb613e60d8e60a20412d80d1a2dd8c45a21582a0aabf008');
INSERT INTO `user` VALUES (2, '2', 'scrypt:32768:8:1$eejsiHtgO2BFI5Ly$7fffa2b5784898d0dfeb868640791545ce0a255a73d06ced4af6f6f68c5e030a6d113805dcd3088b8ae8a5e4c84476b6c5d6c762dab7a47497ad0c3feaf80de1');

SET FOREIGN_KEY_CHECKS = 1;
