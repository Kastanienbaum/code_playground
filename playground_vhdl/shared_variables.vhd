-- 
-- This example shows the behaviour and function of shared variables. 
-- A shared variable can be used in more than one process. 
-- Shared variables were introduced in VHDL-93, refined in VHDL-2008
-- 
-- TODO: 
-- *actually assign values to v_var_shared
--
library IEEE; 
use IEEE.std_logic_1164.all; 
use IEEE.numeric_std; 

entity shared_variables is
  port (
	clk_i : in std_logic;
	reset : in std_logic; 
	a_i   : in std_logic_vector(7 downto 0);
	b_i   : in std_logic_vector(7 downto 0);
	out_o : out std_logic_vector(7 downto 0)
  ) ;
end entity ; -- shared_variables



architecture arch of shared_variables is

	signal s_out : std_logic_vector(7 downto 0); 
	signal s_a : std_logic_vector(7 downto 0);
	signal s_b : std_logic_vector(7 downto 0);


	-- only one process can modify a shared variable, other processes can use (evaluate) it. 
	shared variable v_var_shared : std_logic; 

begin

process_A_RESET : process( clk_i, reset )
begin
	if (clk_i'rising_edge) then
		if (reset = '1') then
			s_a <= (other => '0');
			s_b <= (other => '0');
			s_out <= (other => '0');
		else
		
		end if ;
		
	end if ;
	
end process ; -- process_A_RESET

out_o <= s_out; 


process_B : process( clk_i, reset )
begin
	if (clk_i'rising_edge) then
			
	end if ;
end process ; -- process_B

end architecture ; -- arch
-- EOF 