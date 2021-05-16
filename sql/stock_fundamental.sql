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

 Date: 17/05/2021 02:43:54
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for stock_fundamental
-- ----------------------------
DROP TABLE IF EXISTS `stock_fundamental`;
CREATE TABLE `stock_fundamental`  (
  `id` int(0) NOT NULL COMMENT '主键id',
  `profit` decimal(10, 2) NULL DEFAULT NULL COMMENT '净利润',
  `profit_rate` decimal(10, 2) NULL DEFAULT NULL COMMENT '毛利率',
  `controller` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '实际控制人',
  `shareholders` int(0) NULL DEFAULT NULL COMMENT '股东人数(W)',
  `per_capita` int(0) NULL DEFAULT NULL COMMENT '人均持股数(W)',
  `convergence_rate` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '筹码集中度',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '股票基本面' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
