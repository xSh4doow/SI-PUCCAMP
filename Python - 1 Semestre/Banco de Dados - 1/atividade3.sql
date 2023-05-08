#Experimentos Práticos de Banco de Dados SQL – Lista de Exercícios 03


#	Pedro Rocha 23015967

#1)	Faça os scripts SQL conforme abaixo:

#a.	Crie uma tabela chamada "clientes" com as colunas "id" (chave primária), "nome", "email" e "telefone".
  CREATE TABLE clientes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(50) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  telefone VARCHAR(20));

# b.	Crie uma tabela chamada "pedidos" com as colunas "id" (chave primária), "cliente_id" (chave 
#	estrangeira referenciando a tabela "clientes"), "data" e "total".

	  CREATE TABLE pedidos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  cliente_id INT,
  data DATE NOT NULL,
  total DECIMAL(10, 2) NOT NULL,
  FOREIGN KEY (cliente_id) REFERENCES clientes (id));

#c.	Adicione um registro à tabela "clientes".

	INSERT INTO clientes (nome, email, telefone) VALUES ('Pedro Rocha', 'pedrorocha@gmail.com', '19998878787');


#d.	Adicione dois registros à tabela "pedidos", referenciando o registro adicionado na tabela "clientes".

	INSERT INTO pedidos (cliente_id, data, total) VALUES (1, '2023-05-08', 100.00);
	INSERT INTO pedidos (cliente_id, data, total) VALUES (1, '2023-05-08', 120.00);


# e.	Crie uma tabela chamada "produtos" com as colunas "id" (chave primária), "nome" e "preco".

	  CREATE TABLE produtos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  preco DECIMAL(10, 2) NOT NULL);

# f.	Crie uma tabela chamada "itens_pedido" com as colunas "id" (chave primária), "pedido_id" (chave estrangeira referenciando a tabela "pedidos") e "produto_id" (chave estrangeira referenciando a tabela "produtos").

  CREATE TABLE itens_pedido (
  id INT AUTO_INCREMENT PRIMARY KEY,
  pedido_id INT,
  produto_id INT,
  FOREIGN KEY (pedido_id) REFERENCES pedidos (id),
  FOREIGN KEY (produto_id) REFERENCES produtos (id));


# g.	Adicione dois produtos à tabela "produtos".

	INSERT INTO produtos (nome, preco) VALUES ('Produto 1', 50.00);
	INSERT INTO produtos (nome, preco) VALUES ('Produto 2', 60.00);




# h.	Adicione dois itens ao pedido adicionado anteriormente na tabela "pedidos", referenciando os produtos adicionados na tabela "produtos".

	INSERT INTO itens_pedido (pedido_id, produto_id) VALUES (1, 1);
	INSERT INTO itens_pedido (pedido_id, produto_id) VALUES (1, 2);


# i.	Adicione um registro à tabela "clientes". Adicione três registros à tabela "pedidos", referenciando o registro adicionado na tabela "clientes". Adicione três produtos à tabela "produtos". Adicione três itens ao pedido adicionado anteriormente na tabela "pedidos", referenciando os produtos adicionados na tabela "produtos".

	INSERT INTO clientes (nome, email, telefone) VALUES ('Ordep Ahcor', 'ordep1@gmail.com', '11987766512');
	INSERT INTO pedidos (cliente_id, data, total) VALUES (2, '2023-05-08', 100.00);
	INSERT INTO pedidos (cliente_id, data, total) VALUES (2, '2023-05-08', 200.00);
	INSERT INTO pedidos (cliente_id, data, total) VALUES (2, '2023-05-08', 250.00);

	INSERT INTO produtos (nome, preco) VALUES ('Produto 3', 20.00);
	INSERT INTO produtos (nome, preco) VALUES ('Produto 4', 30.00);
	INSERT INTO produtos (nome, preco) VALUES ('Produto 5', 40.00);

	INSERT INTO itens_pedido (pedido_id, produto_id) VALUES (5, 4);
	INSERT INTO itens_pedido (pedido_id, produto_id) VALUES (5, 4);
	INSERT INTO itens_pedido (pedido_id, produto_id) VALUES (5, 4);

# k.	Crie uma consulta que selecione todos os clientes que possuem pedidos na tabela "pedidos".

	SELECT DISTINCT c.*
	FROM clientes AS c
	JOIN pedidos p ON c.id = p.cliente_id;
	

# l.	Crie uma consulta que retorne o nome e o total gasto por cada cliente.

SELECT c.nome, SUM(p.total) AS total_gasto
FROM clientes AS c
JOIN pedidos AS p 
ON c.id = p.cliente_id
GROUP BY c.id, c.nome;

# m.	Crie uma consulta que retorne o nome do cliente, a data do pedido e o total gasto em cada pedido.

	SELECT c.nome, p.data, p.total
	FROM clientes AS c
	JOIN pedidos AS p 
    ON c.id = p.cliente_id;

# n.	Crie uma consulta que retorne o nome do produto mais vendido, juntamente com o número total de    vezes que ele foi pedido.
	SELECT pr.nome, COUNT(*) AS quantidade_vendida
	FROM itens_pedido AS ip
	JOIN produtos AS pr 
	ON ip.produto_id = pr.id
	GROUP BY ip.produto_id, pr.nome
	ORDER BY quantidade_vendida DESC
	LIMIT 1;

# o.	Crie uma consulta que retorne o nome do cliente que gastou mais em pedidos.

	SELECT c.nome, SUM(p.total) AS total_gasto
	FROM clientes AS c
	JOIN pedidos AS p
    ON c.id = p.cliente_id
	GROUP BY c.id, c.nome
	ORDER BY total_gasto DESC
	LIMIT 1;

# p.	Crie uma consulta que retorne o número de pedidos realizados por cada cliente.

SELECT c.nome, COUNT(*) AS numero_pedidos
FROM clientes AS c
JOIN pedidos AS p 
ON c.id = p.cliente_id
GROUP BY c.id, c.nome;

