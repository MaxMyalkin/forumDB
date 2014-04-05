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
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(50) NOT NULL,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  `username` VARCHAR(45) NULL DEFAULT NULL,
  `isAnonymous` TINYINT NOT NULL DEFAULT false,
  `about` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`email`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `forumDB`.`Forums`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `forumDB`.`Forums` ;

CREATE TABLE IF NOT EXISTS `forumDB`.`Forums` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  `short_name` VARCHAR(50) NOT NULL,
  `user` VARCHAR(50) NOT NULL,
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  UNIQUE INDEX `short_name_UNIQUE` (`short_name` ASC),
  INDEX `fk_Forums_Users_idx` (`user` ASC),
  PRIMARY KEY (`short_name`),
  CONSTRAINT `fk_Forums_Users`
    FOREIGN KEY (`user`)
    REFERENCES `forumDB`.`Users` (`email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `forumDB`.`Threads`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `forumDB`.`Threads` ;

CREATE TABLE IF NOT EXISTS `forumDB`.`Threads` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `date` DATETIME NOT NULL,
  `dislikes` INT NOT NULL DEFAULT 0,
  `isClosed` TINYINT NOT NULL DEFAULT 0,
  `isDeleted` TINYINT NOT NULL DEFAULT 0,
  `likes` INT NOT NULL DEFAULT 0,
  `parentDeleted` TINYINT NOT NULL DEFAULT 0,
  `message` VARCHAR(300) NOT NULL,
  `points` INT NOT NULL DEFAULT 0,
  `posts` INT NOT NULL DEFAULT 0,
  `slug` VARCHAR(45) NOT NULL,
  `title` VARCHAR(100) NOT NULL,
  `user` VARCHAR(50) NOT NULL,
  `forum` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `slug_UNIQUE` (`slug` ASC),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  INDEX `fk_Treads_Users1_idx` (`user` ASC),
  INDEX `fk_Threads_Forums1_idx` (`forum` ASC),
  CONSTRAINT `fk_Treads_Users1`
    FOREIGN KEY (`user`)
    REFERENCES `forumDB`.`Users` (`email`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Threads_Forums1`
    FOREIGN KEY (`forum`)
    REFERENCES `forumDB`.`Forums` (`short_name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `forumDB`.`Posts`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `forumDB`.`Posts` ;

CREATE TABLE IF NOT EXISTS `forumDB`.`Posts` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `date` DATETIME NOT NULL,
  `dislikes` INT NOT NULL DEFAULT 0,
  `isApproved` TINYINT NOT NULL DEFAULT 0,
  `isDeleted` TINYINT NOT NULL DEFAULT 0,
  `isHighlighted` TINYINT NOT NULL DEFAULT 0,
  `isSpam` TINYINT NOT NULL DEFAULT 0,
  `isEdited` TINYINT NOT NULL DEFAULT 0,
  `likes` INT NOT NULL DEFAULT 0,
  `message` VARCHAR(300) NOT NULL,
  `parentDeleted` TINYINT NOT NULL DEFAULT 0,
  `points` INT NOT NULL DEFAULT 0,
  `thread` BIGINT NOT NULL,
  `user` VARCHAR(50) NOT NULL,
  `parent` BIGINT NULL DEFAULT NULL,
  `forum` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  INDEX `fk_Posts_Treads1_idx` (`thread` ASC),
  INDEX `fk_Posts_Users1_idx` (`user` ASC),
  INDEX `fk_Posts_Posts1_idx` (`parent` ASC),
  INDEX `fk_Posts_Forums1_idx` (`forum` ASC),
  CONSTRAINT `fk_Posts_Treads1`
    FOREIGN KEY (`thread`)
    REFERENCES `forumDB`.`Threads` (`id`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Posts_Users1`
    FOREIGN KEY (`user`)
    REFERENCES `forumDB`.`Users` (`email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Posts_Posts1`
    FOREIGN KEY (`parent`)
    REFERENCES `forumDB`.`Posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Posts_Forums1`
    FOREIGN KEY (`forum`)
    REFERENCES `forumDB`.`Forums` (`short_name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `forumDB`.`Followers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `forumDB`.`Followers` ;

CREATE TABLE IF NOT EXISTS `forumDB`.`Followers` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `follower` VARCHAR(50) NOT NULL,
  `followee` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Followers_Users1_idx` (`follower` ASC),
  INDEX `fk_Followers_Users2_idx` (`followee` ASC),
  CONSTRAINT `fk_Followers_Users1`
    FOREIGN KEY (`follower`)
    REFERENCES `forumDB`.`Users` (`email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Followers_Users2`
    FOREIGN KEY (`followee`)
    REFERENCES `forumDB`.`Users` (`email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `forumDB`.`Subscriptions`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `forumDB`.`Subscriptions` ;

CREATE TABLE IF NOT EXISTS `forumDB`.`Subscriptions` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `thread` BIGINT NOT NULL,
  `user` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Subscription_Treads1_idx` (`thread` ASC),
  INDEX `fk_Subscription_Users1_idx` (`user` ASC),
  CONSTRAINT `fk_Subscription_Treads1`
    FOREIGN KEY (`thread`)
    REFERENCES `forumDB`.`Threads` (`id`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Subscription_Users1`
    FOREIGN KEY (`user`)
    REFERENCES `forumDB`.`Users` (`email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
