-- Primeira tentativa de fazer um no
-- 20171012
-- Aguiar

-- Baseado no repositorio de um trabalho feito pra uma disciplina, depois eu coloco de onde saiu.
-- Precisa colocar quantas entradas vamos usar e o tamanho das entradas
-- Precisa definir 

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity Node is
    generic (
        );
    
    Port ( 
        input: in std_logic_vector(7 downto 0);
        );
        
end Node;

architecture Behavioral of Node is
-- Importante lembrar aqui que nao pode usar process pq o circuito nao eh sequencial nem sincrono.
    -- lista signals
    --lista de "fios"
begin
    -- como o circuito se comporta
        
end Behavioral
