/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80019
 Source Host           : localhost:3306
 Source Schema         : stock

 Target Server Type    : MySQL
 Target Server Version : 80019
 File Encoding         : 65001

 Date: 17/05/2021 02:43:44
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for stock_daily
-- ----------------------------
DROP TABLE IF EXISTS `stock_daily`;
CREATE TABLE `stock_daily`  (
  `id` int(0) NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `stock_code` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '股票代码',
  `up_and_down` decimal(5, 2) NULL DEFAULT NULL COMMENT '涨跌幅',
  `symbol` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '符号',
  `turnover_rate` decimal(5, 2) NULL DEFAULT NULL COMMENT '换手率',
  `inflows` decimal(10, 2) NULL DEFAULT NULL COMMENT '资金净流入',
  `create_time` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '股票日常走势' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
