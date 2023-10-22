# aurora-compromise

DEADFACE has taken responsibility for a partial database hack on a pharmacy tied to Aurora Pharmaceuticals. 
The hacked data consists of patient data, staff data, and information on drugs and prescriptions.

We’ve managed to get a hold of the hacked data. 
Provide the first and last name of the patient that lives on a street called Hansons Terrace.

Submit the flag as: flag{First Last}.

## Solution

```sql
CREATE TABLE `patients` (
  `patient_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(32) NOT NULL,
  `last_name` varchar(64) NOT NULL,
  `middle` varchar(8) DEFAULT NULL,
  `sex` varchar(8) NOT NULL,
  `email` varchar(128) NOT NULL,
  `street` varchar(64) NOT NULL,
  `city` varchar(64) NOT NULL,
  `state` varchar(8) NOT NULL,
  `zip` varchar(12) NOT NULL,
  `dob` date NOT NULL,
  PRIMARY KEY (`patient_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=18542 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `patients` VALUES

--(10562,'Sandor','Beyer','V','Male','sbeyer1uz@time.com','20263 Hansons Terrace','Sacramento','CA','94207','1980-05-03')
```

`flag{Sandor Beyer}`
