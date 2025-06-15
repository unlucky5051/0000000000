-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Время создания: Июн 15 2025 г., 08:30
-- Версия сервера: 10.4.32-MariaDB
-- Версия PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `cafe`
--

-- --------------------------------------------------------

--
-- Структура таблицы `drinks`
--

CREATE TABLE `drinks` (
  `id` int(11) NOT NULL,
  `name` varchar(255) CHARACTER SET cp1251 COLLATE cp1251_bin NOT NULL,
  `price` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Дамп данных таблицы `drinks`
--

INSERT INTO `drinks` (`id`, `name`, `price`) VALUES
(1, 'Кола', 95),
(2, 'Апельсиновый сок', 119),
(3, 'Морс брусничный', 149),
(4, 'Чай зеленый', 79),
(5, 'Кофе', 179);

-- --------------------------------------------------------

--
-- Структура таблицы `foods`
--

CREATE TABLE `foods` (
  `id` int(11) NOT NULL,
  `name` varchar(255) CHARACTER SET cp1251 COLLATE cp1251_bin NOT NULL,
  `price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Дамп данных таблицы `foods`
--

INSERT INTO `foods` (`id`, `name`, `price`) VALUES
(1, 'Салат Цезарь', 355),
(2, 'Паста Мясная', 379),
(3, 'Пицца Пепперони', 529),
(4, 'Паста Карбонара', 379),
(5, 'Пицца  Сырная', 409);

-- --------------------------------------------------------

--
-- Структура таблицы `orders`
--

CREATE TABLE `orders` (
  `id` int(10) UNSIGNED NOT NULL,
  `count_cliens` int(11) NOT NULL,
  `table_id` int(11) UNSIGNED NOT NULL,
  `drink_id` int(11) NOT NULL,
  `food_id` int(11) NOT NULL,
  `shift_id` int(11) UNSIGNED NOT NULL,
  `status_id` int(11) UNSIGNED NOT NULL,
  `user_id` int(11) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Дамп данных таблицы `orders`
--

INSERT INTO `orders` (`id`, `count_cliens`, `table_id`, `drink_id`, `food_id`, `shift_id`, `status_id`, `user_id`) VALUES
(7, 1, 1, 1, 1, 1, 4, 2),
(8, 1, 1, 1, 1, 1, 1, 1),
(9, 1, 2, 1, 1, 1, 1, 15),
(10, 1, 2, 1, 1, 1, 5, 13),
(12, 1, 2, 2, 3, 1, 5, 13),
(13, 1, 5, 5, 3, 1, 4, 13);

-- --------------------------------------------------------

--
-- Структура таблицы `roles`
--

CREATE TABLE `roles` (
  `id` int(10) UNSIGNED NOT NULL,
  `role` varchar(255) CHARACTER SET cp1251 COLLATE cp1251_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Дамп данных таблицы `roles`
--

INSERT INTO `roles` (`id`, `role`) VALUES
(1, 'admin'),
(2, 'cook'),
(3, 'waiter'),
(4, 'user');

-- --------------------------------------------------------

--
-- Структура таблицы `shifts`
--

CREATE TABLE `shifts` (
  `id` int(10) UNSIGNED NOT NULL,
  `date` datetime NOT NULL,
  `cook_id` int(11) UNSIGNED NOT NULL,
  `oficiant_1_id` int(11) UNSIGNED NOT NULL,
  `oficiant_2_id` int(11) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Дамп данных таблицы `shifts`
--

INSERT INTO `shifts` (`id`, `date`, `cook_id`, `oficiant_1_id`, `oficiant_2_id`) VALUES
(1, '2024-09-29 10:00:00', 3, 5, 6),
(2, '2024-09-30 09:00:00', 2, 6, 7),
(3, '2024-10-01 11:00:00', 3, 7, 5),
(9, '0000-00-00 00:00:00', 3, 5, 7),
(10, '0000-00-00 00:00:00', 4, 5, 14),
(11, '0000-00-00 00:00:00', 4, 8, 5),
(12, '0000-00-00 00:00:00', 4, 14, 6),
(13, '0000-00-00 00:00:00', 4, 6, 14),
(14, '0000-00-00 00:00:00', 4, 6, 6);

-- --------------------------------------------------------

--
-- Структура таблицы `statuces`
--

CREATE TABLE `statuces` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(255) CHARACTER SET cp1251 COLLATE cp1251_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Дамп данных таблицы `statuces`
--

INSERT INTO `statuces` (`id`, `name`) VALUES
(1, 'Принят'),
(2, 'Оплачен'),
(3, 'Готовится'),
(4, 'Готов'),
(5, 'Отдан');

-- --------------------------------------------------------

--
-- Структура таблицы `tables`
--

CREATE TABLE `tables` (
  `id` int(10) UNSIGNED NOT NULL,
  `number` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Дамп данных таблицы `tables`
--

INSERT INTO `tables` (`id`, `number`) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7);

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `id` int(10) UNSIGNED NOT NULL,
  `login` varchar(255) CHARACTER SET cp1251 COLLATE cp1251_bin NOT NULL,
  `password` varchar(255) CHARACTER SET cp1251 COLLATE cp1251_bin NOT NULL,
  `name` varchar(255) CHARACTER SET cp1251 COLLATE cp1251_bin NOT NULL,
  `role_id` int(11) UNSIGNED NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`id`, `login`, `password`, `name`, `role_id`, `status`) VALUES
(1, 'admin_Ekaterina', '11111', 'Екатерина', 1, 1),
(2, 'cook_Alexandr', '123456', 'Александр', 2, 0),
(3, 'cook_Ivan', 'qwerty', 'Иван', 2, 0),
(4, 'cook_Petr', 'qazxsw', 'Петр', 2, 1),
(5, 'waiter_Anna', '54321', 'Анна', 3, 0),
(6, 'waiter_Ilya', 'Gfhjkm0', 'Илья', 3, 1),
(7, 'waiter_Sergey', 'Пароль0', 'Сергей', 3, 0),
(8, 'waiter_Angelina', 'Angelina89', 'Ангелина', 3, 0),
(12, 'adm', '454545', 'unlucky', 1, 1),
(13, 'Илья', '12345', 'ilya', 4, 1),
(14, '1234', '1234', '1234', 3, 1),
(15, 'user', '11111', 'олег', 4, 0),
(16, 'unlucky', '123', 'qwe', 3, 0),
(20, 'Gele4ka', '12345', 'Ангелина', 1, 0),
(22, '123', '123', '123', 4, 0),
(23, '123', '23', '123', 1, 0),
(24, '123', '123', '123', 4, 0);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `drinks`
--
ALTER TABLE `drinks`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `foods`
--
ALTER TABLE `foods`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`),
  ADD KEY `drink_id` (`drink_id`),
  ADD KEY `food_id` (`food_id`),
  ADD KEY `shift_id` (`shift_id`),
  ADD KEY `status_id` (`status_id`),
  ADD KEY `table_id` (`table_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Индексы таблицы `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `shifts`
--
ALTER TABLE `shifts`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cook` (`cook_id`),
  ADD KEY `oficiant_1` (`oficiant_1_id`),
  ADD KEY `oficiant_2` (`oficiant_2_id`);

--
-- Индексы таблицы `statuces`
--
ALTER TABLE `statuces`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `tables`
--
ALTER TABLE `tables`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD KEY `role_id` (`role_id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `drinks`
--
ALTER TABLE `drinks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `foods`
--
ALTER TABLE `foods`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT для таблицы `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `shifts`
--
ALTER TABLE `shifts`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT для таблицы `statuces`
--
ALTER TABLE `statuces`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `tables`
--
ALTER TABLE `tables`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`drink_id`) REFERENCES `drinks` (`id`),
  ADD CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`food_id`) REFERENCES `foods` (`id`),
  ADD CONSTRAINT `orders_ibfk_3` FOREIGN KEY (`shift_id`) REFERENCES `shifts` (`id`),
  ADD CONSTRAINT `orders_ibfk_4` FOREIGN KEY (`status_id`) REFERENCES `statuces` (`id`),
  ADD CONSTRAINT `orders_ibfk_5` FOREIGN KEY (`table_id`) REFERENCES `tables` (`id`),
  ADD CONSTRAINT `orders_ibfk_6` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Ограничения внешнего ключа таблицы `shifts`
--
ALTER TABLE `shifts`
  ADD CONSTRAINT `shifts_ibfk_1` FOREIGN KEY (`cook_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `shifts_ibfk_2` FOREIGN KEY (`oficiant_1_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `shifts_ibfk_3` FOREIGN KEY (`oficiant_2_id`) REFERENCES `users` (`id`);

--
-- Ограничения внешнего ключа таблицы `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
