SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";



CREATE TABLE `from` (
  `city_id` int(10) UNSIGNED NOT NULL,
  `city_name` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `city`
--

INSERT INTO `from` (`city_id`, `city_name`) VALUES
(1, 'Banglore'),
(2, 'Hyderabad'),
(3, 'Chennai');

CREATE TABLE `to` (
  `city_id` int(10) UNSIGNED NOT NULL,
  `city_name` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `city`
--

INSERT INTO `to` (`city_id`, `city_name`) VALUES
(1, 'Banglore'),
(2, 'Hyderabad'),
(3, 'Chennai');




CREATE TABLE `way` (
  `way_id` int(10) UNSIGNED NOT NULL,
  `way_name` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `city`
--

INSERT INTO `way` (`way_id`, `way_name`) VALUES
(1, '1 way'),
(2, '2 way');





CREATE TABLE `vehicle_type` (
  `vehicle_id` int(10) UNSIGNED NOT NULL,
  `vehicle_name` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `city`
--

INSERT INTO `vehicle_type` (`vehicle_id`, `vehicle_name`) VALUES
(1, 'car/jeep'),
(2, 'lorry/truck'),
(3, 'bus');






CREATE TABLE `register` (
  `register_id` int(11) NOT NULL,
  `register_first` varchar(255) NOT NULL,
  `register_last` varchar(255) NOT NULL,
  `register_email` varchar(255) NOT NULL,
  `register_mobile` varchar(255) NOT NULL,
  `registe_password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 ROW_FORMAT=COMPACT;

--
-- Dumping data for table `customer`
--





CREATE TABLE `tolls` (
  `tolls_id` int(10) UNSIGNED NOT NULL,
  `tolls_name` varchar(45) NOT NULL,
  `tolls_from` varchar(45) NOT NULL,
  `tolls_to` varchar(45) NOT NULL,
  `tolls_price` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
--
-- Dumping data for table `city`
--
ALTER TABLE `from`
  ADD PRIMARY KEY (`city_id`);

--
-- Indexes for table `country`
--
ALTER TABLE `to`
  ADD PRIMARY KEY (`city_id`);

--
-- Indexes for table `customer`
--
ALTER TABLE `way`
  ADD PRIMARY KEY (`way_id`);

--
-- Indexes for table `department`
--
ALTER TABLE `vehicle_type`
  ADD PRIMARY KEY (`vehicle_id`);

--
-- Indexes for table `employee`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`register_id`);

--
-- Indexes for table `login`
--
ALTER TABLE `tolls`
  ADD PRIMARY KEY (`tolls_id`);



ALTER TABLE `from`
  MODIFY `city_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `country`
--
ALTER TABLE `to`
  MODIFY `city_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `way`
  MODIFY `way_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `department`
--
ALTER TABLE `vehicle_type`
  MODIFY `vehicle_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `register`
  MODIFY `register_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `tolls`
  MODIFY `tolls_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;









