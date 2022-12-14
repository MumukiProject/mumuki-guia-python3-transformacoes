class Test(unittest.TestCase):
  
  def test_cruzeiros_tem_coluna_region(self):
    self.assertTrue("region" em cruzeiros.colunas)
    

  def test_cruzeiros_no_brasil_são_regionais(self):
    indexado = cruises.set_index("cruise_id")
    
    self.assertEquals(indexed.loc[10404, "region"], "Regional")
    self.assertEquals(indexed.loc[1494, "region"], "Regional")
    self.assertEquals(indexed.loc[11099, "region"], "Regional")
    

  def test_cruzeiros_da_argentina_são_regionais(self):
    indexado = cruises.set_index("cruise_id")
    
    self.assertEquals(indexed.loc[5296, "region"], "Regional")
    self.assertEquals(indexed.loc[2537, "region"], "Regional")
    self.assertEquals(indexed.loc[7237, "region"], "Regional")
    
  def test_cruzeiros_uruguaios_são_nacionais(self):
    indexado = cruises.set_index("cruise_id")
    
    self.assertEquals(indexed.loc[5823, "region"], "Nacional")
    
  def test_cruzeiros_nos_EUA_não_são_regionais(self):
    indexado = cruises.set_index("cruise_id")
    
    self.assertEquals(indexed.loc[8829, "region"], "Não regional")
    

  def test_cruzeiros_de_outro_país_na_Ásia_não_são_regionais(self):
    indexado = cruises.set_index("cruise_id")
    
    self.assertEquals(indexed.loc[7638, "region"], "Não regional")