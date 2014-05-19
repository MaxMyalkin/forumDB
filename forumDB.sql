SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

DROP SCHEMA IF EXISTS `forumDB` ;
CREATE SCHEMA IF NOT EXISTS `forumDB` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `forumDB` ;

-- -----------------------------------------------------
-- Table `forumDB`.`Users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `forumDB`.`Users` ;

CREATE TABLE IF NOT EXISTS `forumDB`.`Users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(50) NOT NULL,
  `name` VARCHAR(100) NULL DEFAULT NULL,
  `username` VARCHAR(80) NULL DEFAULT NULL,
  `isAnonymous` TINYINT NOT NULL DEFAULT false,
  `about` VARCHAR(150) NULL DEFAULT NULL,
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  PRIMARY KEY (`email`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `forumDB`.`Forums`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `forumDB`.`Forums` ;

CREATE TABLE IF NOT EXISTS `forumDB`.`Forums` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `short_name` VARCHAR(50) NOT NULL,
  `user` VARCHAR(50) NOT NULL,
  INDEX `fk_Forums_Users_idx` (`user` ASC),
  PRIMARY KEY (`short_name`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  CONSTRAINT `fk_Forums_Users`
    FOREIGN KEY (`user`)
    REFERENCES `forumDB`.`Users` (`email`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `forumDB`.`Threads`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `forumDB`.`Threads` ;

CREATE TABLE IF NOT EXISTS `forumDB`.`Threads` (
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
  `user` VARCHAR(50) NOT NULL,
  `forum` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_forum_date` (`forum` ASC, `date` ASC),
  INDEX `idx_user_date` (`user` ASC, `date` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `forumDB`.`Posts`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `forumDB`.`Posts` ;

CREATE TABLE IF NOT EXISTS `forumDB`.`Posts` (
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
  `user` VARCHAR(50) NOT NULL,
  `forum` VARCHAR(50) NOT NULL,
  `u_id` INT UNSIGNED NOT NULL,
  `parent` INT UNSIGNED NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Posts_Treads1_idx` (`thread` ASC),
  INDEX `fk_Posts_Users1_idx` (`user` ASC),
  INDEX `idx_forum_date` (`forum` ASC, `date` ASC),
  INDEX `idx_forum_uid` (`forum` ASC, `u_id` ASC),
  CONSTRAINT `fk_Posts_Treads1`
    FOREIGN KEY (`thread`)
    REFERENCES `forumDB`.`Threads` (`id`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Posts_Users1`
    FOREIGN KEY (`user`)
    REFERENCES `forumDB`.`Users` (`email`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Posts_Forums1`
    FOREIGN KEY (`forum`)
    REFERENCES `forumDB`.`Forums` (`short_name`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `forumDB`.`Followers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `forumDB`.`Followers` ;

CREATE TABLE IF NOT EXISTS `forumDB`.`Followers` (
  `followee` VARCHAR(50) NOT NULL,
  `follower` VARCHAR(50) NOT NULL,
  INDEX `fk_Followers_Users2_idx` (`followee` ASC),
  INDEX `fk_Followers_Users1_idx` (`follower` ASC),
  CONSTRAINT `fk_Followers_Users2`
    FOREIGN KEY (`followee`)
    REFERENCES `forumDB`.`Users` (`email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Followers_Users1`
    FOREIGN KEY (`follower`)
    REFERENCES `forumDB`.`Users` (`email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `forumDB`.`Subscriptions`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `forumDB`.`Subscriptions` ;

CREATE TABLE IF NOT EXISTS `forumDB`.`Subscriptions` (
  `thread` INT NOT NULL,
  `user` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`user`, `thread`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
