SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

DROP SCHEMA IF EXISTS `forumDB_ID` ;
CREATE SCHEMA IF NOT EXISTS `forumDB_ID` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `forumDB_ID` ;

-- -----------------------------------------------------
-- Table `forumDB_ID`.`Users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `forumDB_ID`.`Users` ;

CREATE TABLE IF NOT EXISTS `forumDB_ID`.`Users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(50) NOT NULL,
  `name` VARCHAR(100) NULL DEFAULT NULL,
  `username` VARCHAR(80) NULL DEFAULT NULL,
  `isAnonymous` TINYINT NOT NULL DEFAULT false,
  `about` VARCHAR(150) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `email_id` (`email` ASC, `id` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `forumDB_ID`.`Forums`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `forumDB_ID`.`Forums` ;

CREATE TABLE IF NOT EXISTS `forumDB_ID`.`Forums` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `short_name` VARCHAR(50) NOT NULL,
  `u_id` INT NOT NULL,
  `user` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Forums_Users1_idx` (`u_id` ASC),
  INDEX `idx_shortname_id` (`short_name` ASC, `id` ASC),
  CONSTRAINT `fk_Forums_Users1`
    FOREIGN KEY (`u_id`)
    REFERENCES `forumDB_ID`.`Users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `forumDB_ID`.`Threads`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `forumDB_ID`.`Threads` ;

CREATE TABLE IF NOT EXISTS `forumDB_ID`.`Threads` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `date` DATETIME NOT NULL,
  `dislikes` INT UNSIGNED NOT NULL DEFAULT 0,
  `isClosed` TINYINT NOT NULL DEFAULT 0,
  `isDeleted` TINYINT NOT NULL DEFAULT 0,
  `likes` INT UNSIGNED NOT NULL DEFAULT 0,
  `message` TEXT NOT NULL,
  `points` INT NOT NULL DEFAULT 0,
  `posts` INT UNSIGNED NOT NULL DEFAULT 0,
  `slug` VARCHAR(80) NOT NULL,
  `title` VARCHAR(100) NOT NULL,
  `u_id` INT NOT NULL,
  `f_id` INT UNSIGNED NOT NULL,
  `user` VARCHAR(50) NOT NULL,
  `forum` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_fid_date` (`f_id` ASC, `date` ASC),
  INDEX `idx_uid_date` (`u_id` ASC, `date` ASC),
  CONSTRAINT `fk_Threads_Users1`
    FOREIGN KEY (`u_id`)
    REFERENCES `forumDB_ID`.`Users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Threads_Forums1`
    FOREIGN KEY (`f_id`)
    REFERENCES `forumDB_ID`.`Forums` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `forumDB_ID`.`Posts`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `forumDB_ID`.`Posts` ;

CREATE TABLE IF NOT EXISTS `forumDB_ID`.`Posts` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `date` DATETIME NOT NULL,
  `dislikes` INT UNSIGNED NOT NULL DEFAULT 0,
  `isApproved` TINYINT NOT NULL DEFAULT 0,
  `isDeleted` TINYINT NOT NULL DEFAULT 0,
  `isHighlighted` TINYINT NOT NULL DEFAULT 0,
  `isSpam` TINYINT NOT NULL DEFAULT 0,
  `isEdited` TINYINT NOT NULL DEFAULT 0,
  `likes` INT UNSIGNED NOT NULL DEFAULT 0,
  `message` TEXT NOT NULL,
  `points` INT NOT NULL DEFAULT 0,
  `thread` INT UNSIGNED NOT NULL,
  `parent` INT UNSIGNED NULL,
  `f_id` INT UNSIGNED NOT NULL,
  `u_id` INT NOT NULL,
  `user` VARCHAR(50) NOT NULL,
  `forum` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_fid_date` (`f_id` ASC, `date` ASC),
  INDEX `idx_fid_uid` (`f_id` ASC, `u_id` ASC),
  INDEX `idx_uid_date` (`u_id` ASC, `date` ASC),
  INDEX `idx_thread_date` (`thread` ASC, `date` ASC),
  CONSTRAINT `fk_Posts_Forums1`
    FOREIGN KEY (`f_id`)
    REFERENCES `forumDB_ID`.`Forums` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Posts_Users1`
    FOREIGN KEY (`u_id`)
    REFERENCES `forumDB_ID`.`Users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `forumDB_ID`.`Followers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `forumDB_ID`.`Followers` ;

CREATE TABLE IF NOT EXISTS `forumDB_ID`.`Followers` (
  `follower` INT NOT NULL,
  `followee` INT NOT NULL,
  INDEX `follower_ee` (`follower` ASC, `followee` ASC),
  INDEX `followee_er` (`followee` ASC, `follower` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `forumDB_ID`.`Subscriptions`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `forumDB_ID`.`Subscriptions` ;

CREATE TABLE IF NOT EXISTS `forumDB_ID`.`Subscriptions` (
  `thread` INT NOT NULL,
  `u_id` INT NOT NULL,
  `user` VARCHAR(50) NULL,
  PRIMARY KEY (`u_id`, `thread`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
