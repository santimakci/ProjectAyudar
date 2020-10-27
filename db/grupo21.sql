-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 27-10-2020 a las 19:51:39
-- Versión del servidor: 10.1.44-MariaDB-0ubuntu0.18.04.1
-- Versión de PHP: 7.2.24-0ubuntu0.18.04.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `grupo21`
--
CREATE DATABASE IF NOT EXISTS `grupo21` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `grupo21`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pageSettings`
--

CREATE TABLE `pageSettings` (
  `id` int(11) NOT NULL,
  `email` varchar(30) DEFAULT NULL,
  `description` text,
  `title` varchar(255) CHARACTER SET latin1 COLLATE latin1_spanish_ci NOT NULL,
  `enabled` tinyint(1) NOT NULL,
  `elements` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `pageSettings`
--

INSERT INTO `pageSettings` (`id`, `email`, `description`, `title`, `enabled`, `elements`) VALUES
(1, 'ayudar@ayudar.com.ar', 'La mejor página @juli aprobanos', 'ayudAR', 1, 5),
(2, 'jose@mail.com', 'El sistema de dice que hay un error', '', 0, 0),
(4, 'maria@mail.com', 'No tengo acceso al sistema', '', 0, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `permissions`
--

CREATE TABLE `permissions` (
  `id` int(11) NOT NULL,
  `name` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `id` int(11) NOT NULL,
  `name` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`id`, `name`) VALUES
(1, 'admin'),
(4, 'operator');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rolesPermissions`
--

CREATE TABLE `rolesPermissions` (
  `id` int(11) NOT NULL,
  `rol_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(11) UNSIGNED NOT NULL,
  `email` varchar(30) NOT NULL,
  `password` varchar(255) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `username` varchar(20) CHARACTER SET latin1 COLLATE latin1_spanish_ci NOT NULL,
  `active` tinyint(1) NOT NULL,
  `date_updated` datetime NOT NULL,
  `date_created` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `email`, `password`, `first_name`, `last_name`, `username`, `active`, `date_updated`, `date_created`) VALUES
(1, 'admin', '123123', 'Cosme', 'Fulanito', 'admin', 1, '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(2, 'santimakcimovich@gmail.com', '123', 'Santiago', 'Makcimovich', 'santi', 1, '2020-10-18 23:48:24', '2020-10-18 23:48:24'),
(3, 'vero@gmail.com', 'vero', 'vero', 'isoardi', 'veroiso', 1, '2020-10-18 23:49:16', '2020-10-18 23:49:16'),
(6, 'veroisoardi@gmail.com', 'vero', 'veronica', 'isoardi', 'veroisoardi', 1, '2020-10-19 00:03:04', '2020-10-19 00:03:04'),
(7, 'admin@admin.com', '123', 'Gaston', 'Ginestet', 'Gaston', 1, '2020-10-19 00:03:15', '2020-10-19 00:03:15');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usersRoles`
--

CREATE TABLE `usersRoles` (
  `id` int(11) NOT NULL,
  `rol_id` int(11) NOT NULL,
  `user_id` int(11) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `usersRoles`
--

INSERT INTO `usersRoles` (`id`, `rol_id`, `user_id`) VALUES
(1, 1, 1),
(2, 4, 2),
(3, 4, 3),
(4, 4, 6),
(5, 1, 7);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `pageSettings`
--
ALTER TABLE `pageSettings`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `permissions`
--
ALTER TABLE `permissions`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `rolesPermissions`
--
ALTER TABLE `rolesPermissions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_rool` (`rol_id`),
  ADD KEY `id_permiso` (`permission_id`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `username` (`username`),
  ADD KEY `activo` (`active`);

--
-- Indices de la tabla `usersRoles`
--
ALTER TABLE `usersRoles`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_rol` (`rol_id`),
  ADD KEY `id_usuario` (`user_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `pageSettings`
--
ALTER TABLE `pageSettings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT de la tabla `permissions`
--
ALTER TABLE `permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT de la tabla `rolesPermissions`
--
ALTER TABLE `rolesPermissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT de la tabla `usersRoles`
--
ALTER TABLE `usersRoles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `rolesPermissions`
--
ALTER TABLE `rolesPermissions`
  ADD CONSTRAINT `id_permiso` FOREIGN KEY (`permission_id`) REFERENCES `permissions` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `id_rool` FOREIGN KEY (`rol_id`) REFERENCES `roles` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `usersRoles`
--
ALTER TABLE `usersRoles`
  ADD CONSTRAINT `id_rol` FOREIGN KEY (`rol_id`) REFERENCES `roles` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `id_usuario` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
