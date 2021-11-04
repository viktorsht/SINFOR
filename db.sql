-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Tempo de geração: 04-Nov-2021 às 18:53
-- Versão do servidor: 10.5.12-MariaDB-cll-lve
-- versão do PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `u831868453_Eva`
--

DELIMITER $$
--
-- Procedimentos
--
$$

$$

$$

--
-- Funções
--
$$

$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estrutura da tabela `acs`
--

CREATE TABLE `acs` (
  `id` int(11) NOT NULL,
  `cod_ma` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `acs`
--

INSERT INTO `acs` (`id`, `cod_ma`, `nome`) VALUES
(1, 123, 'Eva'),
(2, 25, 'Maria'),
(3, 207, 'Joao'),
(4, 42, 'Ivan'),
(5, 33, 'Paulo');

-- --------------------------------------------------------

--
-- Estrutura da tabela `agendado`
--

CREATE TABLE `agendado` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `cpf` varchar(11) COLLATE utf8mb4_unicode_ci NOT NULL,
  `num_sus` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  `data_1dose` date DEFAULT NULL,
  `data_2dose` date DEFAULT NULL,
  `fk_vacina` int(11) DEFAULT NULL,
  `fk_cod_ubs` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Extraindo dados da tabela `agendado`
--

INSERT INTO `agendado` (`id`, `nome`, `cpf`, `num_sus`, `data_1dose`, `data_2dose`, `fk_vacina`, `fk_cod_ubs`) VALUES
(1, 'Emanuel', '1234567', '123456789', '2021-05-18', '2021-06-08', 2, 1),
(2, 'Aline', '0000000', '00000000', '2021-04-18', '2021-05-09', 3, 4),
(3, 'Jose', '111111111', '1111111111111', '2021-05-18', '2021-06-08', 1, 2),
(4, 'Samuel', '2222222', '2222222222', '2021-05-18', '2021-08-06', 2, 3),
(5, 'Veronica', '33333333', '33333333333', '2021-04-18', '2021-07-07', 2, 5);

--
-- Acionadores `agendado`
--
DELIMITER $$
CREATE TRIGGER `agendado_log_delete` AFTER DELETE ON `agendado` FOR EACH ROW INSERT INTO agendado_log (old_id_agendado, old_nm_agendado, new_id_agendado, new_nm_agendado, 
          evento, usuario, data_hora)
          VALUES (OLD.id, OLD.nome, NULL, NULL, 'DELETE', USER(), NOW())
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `agendado_log_insert` AFTER INSERT ON `agendado` FOR EACH ROW INSERT INTO agendado_log (old_id_agendado, old_nm_agendado, new_id_agendado, new_nm_agendado, 
          evento, usuario, data_hora)
          VALUES (NULL, NULL, NEW.id, NEW.nome, 'INSERT', USER(), NOW())
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `agendado_log_update` AFTER UPDATE ON `agendado` FOR EACH ROW INSERT INTO agendado_log (old_id_agendado, old_nm_agendado, new_id_agendado, new_nm_agendado, 
          evento, usuario, data_hora)
          VALUES (OLD.id, OLD.nome, NEW.id, NEW.nome, 'UPDATE', USER(), NOW())
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estrutura da tabela `agendado_log`
--

CREATE TABLE `agendado_log` (
  `id_agendado_log` int(11) NOT NULL,
  `old_id_agendado` int(11) DEFAULT NULL,
  `old_nm_agendado` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `new_id_agendado` int(11) DEFAULT NULL,
  `new_nm_agendado` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `evento` varchar(6) COLLATE utf8mb4_unicode_ci NOT NULL,
  `usuario` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `data_hora` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Extraindo dados da tabela `agendado_log`
--

INSERT INTO `agendado_log` (`id_agendado_log`, `old_id_agendado`, `old_nm_agendado`, `new_id_agendado`, `new_nm_agendado`, `evento`, `usuario`, `data_hora`) VALUES
(1, 1, 'Emanuel', 1, 'Emanuel', 'UPDATE', 'u831868453_Eva@127.0.0.1', '2021-07-04 22:31:22'),
(2, 2, 'Aline', 2, 'Aline', 'UPDATE', 'u831868453_Eva@127.0.0.1', '2021-07-04 22:31:27'),
(5, 4, 'Samuel', 4, 'Samuel', 'UPDATE', 'u831868453_Eva@127.0.0.1', '2021-07-04 22:31:38'),
(6, 5, 'Veronica', 5, 'Veronica', 'UPDATE', 'u831868453_Eva@127.0.0.1', '2021-07-04 22:31:41');

-- --------------------------------------------------------

--
-- Estrutura da tabela `comunitario`
--

CREATE TABLE `comunitario` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `num_sus` varchar(15) NOT NULL,
  `status_1dose` tinyint(4) DEFAULT NULL,
  `data_1dose` date DEFAULT NULL,
  `status_2dose` int(4) DEFAULT NULL,
  `data_2dose` date DEFAULT NULL,
  `fk_cod_acs` int(11) NOT NULL,
  `fk_vacina_tipo` int(11) DEFAULT NULL,
  `fk_cod_ubs` int(11) NOT NULL,
  `fk_lote_d1` int(11) DEFAULT NULL,
  `fk_lote_d2` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `comunitario`
--

INSERT INTO `comunitario` (`id`, `nome`, `cpf`, `num_sus`, `status_1dose`, `data_1dose`, `status_2dose`, `data_2dose`, `fk_cod_acs`, `fk_vacina_tipo`, `fk_cod_ubs`, `fk_lote_d1`, `fk_lote_d2`) VALUES
(1, 'Emanuel', '1234567', '123456789', 1, '2021-05-18', 0, '0000-00-00', 1, 1, 4, 3, NULL),
(4, 'Samnuel', '22222222222', '222222222222222', 1, '2021-05-18', 0, '2021-08-06', 2, 3, 2, 2, NULL),
(5, 'Juliana', '99999999', '999999999999', 1, '2021-02-02', 1, '2021-02-23', 2, 1, 3, 1, 2),
(7, 'Caio', '55555555', '55555555555', 1, '2021-01-10', 1, '2021-04-10', 4, 3, 1, 3, 3);

-- --------------------------------------------------------

--
-- Estrutura da tabela `laboratorio`
--

CREATE TABLE `laboratorio` (
  `id` int(11) NOT NULL,
  `nome` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `laboratorio`
--

INSERT INTO `laboratorio` (`id`, `nome`) VALUES
(1, 'Butantan'),
(2, 'Oxford/Fiocruz'),
(3, 'BioNTech'),
(4, 'Instituto Gamaleya');

--
-- Acionadores `laboratorio`
--
DELIMITER $$
CREATE TRIGGER `lab_log_delete` AFTER DELETE ON `laboratorio` FOR EACH ROW INSERT INTO lab_log (old_id_lab, old_nm_lab, new_id_lab, new_nm_lab, 
          evento, usuario, data_hora)
          VALUES (OLD.id, OLD.nome, NULL, NULL, 'DELETE', USER(), NOW())
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `lab_log_insert` AFTER INSERT ON `laboratorio` FOR EACH ROW INSERT INTO lab_log (old_id_lab, old_nm_lab, new_id_lab, new_nm_lab, 
          evento, usuario, data_hora)
          VALUES (NULL, NULL, NEW.id, NEW.nome, 'INSERT', USER(), NOW())
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `lab_log_update` AFTER UPDATE ON `laboratorio` FOR EACH ROW INSERT INTO lab_log (old_id_lab, old_nm_lab, new_id_lab, new_nm_lab, 
          evento, usuario, data_hora)
          VALUES (OLD.id, OLD.nome, NEW.id, NEW.nome, 'UPDATE', USER(), NOW())
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estrutura da tabela `lab_log`
--

CREATE TABLE `lab_log` (
  `id_lab_log` int(11) NOT NULL,
  `old_id_lab` int(11) DEFAULT NULL,
  `old_nm_lab` varchar(60) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `new_id_lab` int(11) DEFAULT NULL,
  `new_nm_lab` varchar(60) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `evento` varchar(6) COLLATE utf8mb4_unicode_ci NOT NULL,
  `usuario` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `data_hora` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Extraindo dados da tabela `lab_log`
--

INSERT INTO `lab_log` (`id_lab_log`, `old_id_lab`, `old_nm_lab`, `new_id_lab`, `new_nm_lab`, `evento`, `usuario`, `data_hora`) VALUES
(1, NULL, NULL, 11, 'Johnson', 'INSERT', 'u831868453_Eva@45.179.115.44', '2021-07-15 14:27:46'),
(2, 11, 'Johnson', 11, 'Johnson & Johnson', 'UPDATE', 'u831868453_Eva@45.179.115.44', '2021-07-15 14:28:14'),
(3, 11, 'Johnson & Johnson', NULL, NULL, 'DELETE', 'u831868453_Eva@45.179.115.44', '2021-07-15 14:28:42');

-- --------------------------------------------------------

--
-- Estrutura da tabela `lote_vacina`
--

CREATE TABLE `lote_vacina` (
  `id` int(11) NOT NULL,
  `fk_vacina` int(11) NOT NULL,
  `lote` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  `fabricacao` date NOT NULL,
  `validade` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Extraindo dados da tabela `lote_vacina`
--

INSERT INTO `lote_vacina` (`id`, `fk_vacina`, `lote`, `fabricacao`, `validade`) VALUES
(1, 1, '1234ABCD', '2021-02-02', '2021-04-02'),
(2, 1, 'ABCD1234', '2021-03-02', '2021-05-02'),
(3, 2, 'QWE1234', '2021-01-12', '2021-04-12'),
(4, 3, 'ZRTW', '2020-12-26', '2021-03-26');

-- --------------------------------------------------------

--
-- Estrutura da tabela `nivel_acesso`
--

CREATE TABLE `nivel_acesso` (
  `id` int(11) NOT NULL,
  `nome` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Extraindo dados da tabela `nivel_acesso`
--

INSERT INTO `nivel_acesso` (`id`, `nome`) VALUES
(2, 'Adm_sec'),
(3, 'acs'),
(4, 'adm_ubs'),
(5, 'comunitario');

-- --------------------------------------------------------

--
-- Estrutura da tabela `sec_saude`
--

CREATE TABLE `sec_saude` (
  `id` int(11) NOT NULL,
  `nome` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `sec_saude`
--

INSERT INTO `sec_saude` (`id`, `nome`) VALUES
(1, 'PICOS - PI ');

-- --------------------------------------------------------

--
-- Estrutura da tabela `ubs`
--

CREATE TABLE `ubs` (
  `id` int(11) NOT NULL,
  `cod_ubs` int(11) NOT NULL,
  `nome` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `ubs`
--

INSERT INTO `ubs` (`id`, `cod_ubs`, `nome`) VALUES
(1, 12, 'Ipueiras'),
(2, 47, 'Vicente Baldino'),
(3, 35, 'Passagem das Pedras'),
(4, 20, 'Saude de Morrinhos'),
(5, 5, 'Saude da Paraibinha');

-- --------------------------------------------------------

--
-- Estrutura da tabela `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `usuario` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  `senha` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  `nivel_de_acesso` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Extraindo dados da tabela `usuario`
--

INSERT INTO `usuario` (`id`, `usuario`, `senha`, `email`, `nivel_de_acesso`) VALUES
(1, 'Eva', '202cb962ac59075b964b07152d234b70', 'eva.luana@hotmail.com', 2),
(2, 'Eva', '202cb962ac59075b964b07152d234b70', 'eva.luana@hotmail.com', 2),
(3, 'Doralice', '289dff07669d7a23de0ef88d2f7129e7', 'dora.lice@hotmail.com', 2),
(4, 'Marcelo', 'f5b330d2ea9015fb7c41ddbe7268d245', 'Mar.lima@hotmail.com', 3),
(5, 'Emanuel', '9fe8593a8a330607d76796b35c64c600', 'emanuel123@gmail.com', 4),
(6, 'Severina', 'd840cc5d906c3e9c84374c8919d2074e', 'sev.2018@hotmail.com', 2);

-- --------------------------------------------------------

--
-- Estrutura da tabela `vacina`
--

CREATE TABLE `vacina` (
  `id` int(11) NOT NULL,
  `nome` varchar(45) NOT NULL,
  `reforco` int(11) NOT NULL,
  `laboratorio` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `vacina`
--

INSERT INTO `vacina` (`id`, `nome`, `reforco`, `laboratorio`) VALUES
(1, 'Coronavac', 21, 1),
(2, 'Pfizer', 90, 3),
(3, 'Astrazeneca', 90, 2),
(4, 'Sputnik V', 90, 4);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `acs`
--
ALTER TABLE `acs`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `agendado`
--
ALTER TABLE `agendado`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk__vacina` (`fk_vacina`),
  ADD KEY `fk_cod_ubs` (`fk_cod_ubs`);

--
-- Índices para tabela `agendado_log`
--
ALTER TABLE `agendado_log`
  ADD PRIMARY KEY (`id_agendado_log`);

--
-- Índices para tabela `comunitario`
--
ALTER TABLE `comunitario`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_lote_d1` (`fk_lote_d1`),
  ADD KEY `fk_lote_d2` (`fk_lote_d2`),
  ADD KEY `cod_acs` (`fk_cod_acs`),
  ADD KEY `cod_ubs` (`fk_cod_ubs`),
  ADD KEY `vacina_tipo` (`fk_vacina_tipo`);

--
-- Índices para tabela `laboratorio`
--
ALTER TABLE `laboratorio`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `lab_log`
--
ALTER TABLE `lab_log`
  ADD PRIMARY KEY (`id_lab_log`);

--
-- Índices para tabela `lote_vacina`
--
ALTER TABLE `lote_vacina`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_vacina` (`fk_vacina`);

--
-- Índices para tabela `nivel_acesso`
--
ALTER TABLE `nivel_acesso`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `sec_saude`
--
ALTER TABLE `sec_saude`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `ubs`
--
ALTER TABLE `ubs`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_nivel_de_acesso` (`nivel_de_acesso`);

--
-- Índices para tabela `vacina`
--
ALTER TABLE `vacina`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_laboratorio` (`laboratorio`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `acs`
--
ALTER TABLE `acs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `agendado`
--
ALTER TABLE `agendado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `agendado_log`
--
ALTER TABLE `agendado_log`
  MODIFY `id_agendado_log` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de tabela `comunitario`
--
ALTER TABLE `comunitario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de tabela `laboratorio`
--
ALTER TABLE `laboratorio`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de tabela `lab_log`
--
ALTER TABLE `lab_log`
  MODIFY `id_lab_log` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `lote_vacina`
--
ALTER TABLE `lote_vacina`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de tabela `nivel_acesso`
--
ALTER TABLE `nivel_acesso`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `ubs`
--
ALTER TABLE `ubs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de tabela `vacina`
--
ALTER TABLE `vacina`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `agendado`
--
ALTER TABLE `agendado`
  ADD CONSTRAINT `fk__vacina` FOREIGN KEY (`fk_vacina`) REFERENCES `vacina` (`id`),
  ADD CONSTRAINT `fk_cod_ubs` FOREIGN KEY (`fk_cod_ubs`) REFERENCES `ubs` (`id`);

--
-- Limitadores para a tabela `comunitario`
--
ALTER TABLE `comunitario`
  ADD CONSTRAINT `fk_cod_acs` FOREIGN KEY (`fk_cod_acs`) REFERENCES `acs` (`id`),
  ADD CONSTRAINT `fk_lote_d1` FOREIGN KEY (`fk_lote_d1`) REFERENCES `lote_vacina` (`id`),
  ADD CONSTRAINT `fk_lote_d2` FOREIGN KEY (`fk_lote_d2`) REFERENCES `lote_vacina` (`id`),
  ADD CONSTRAINT `fk_ubs_` FOREIGN KEY (`fk_cod_ubs`) REFERENCES `ubs` (`id`),
  ADD CONSTRAINT `fk_vacina_tipo` FOREIGN KEY (`fk_vacina_tipo`) REFERENCES `vacina` (`id`);

--
-- Limitadores para a tabela `lote_vacina`
--
ALTER TABLE `lote_vacina`
  ADD CONSTRAINT `fk_vacina` FOREIGN KEY (`fk_vacina`) REFERENCES `vacina` (`id`);

--
-- Limitadores para a tabela `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `fk_nivel_de_acesso` FOREIGN KEY (`nivel_de_acesso`) REFERENCES `nivel_acesso` (`id`);

--
-- Limitadores para a tabela `vacina`
--
ALTER TABLE `vacina`
  ADD CONSTRAINT `fk_laboratorio` FOREIGN KEY (`laboratorio`) REFERENCES `laboratorio` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
