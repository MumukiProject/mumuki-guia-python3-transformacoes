class Test(unittest.TestCase):
  
  def test_cruceros_tiene_columna_region(self):
    self.assertTrue("region" in cruceros.columns)
    

  def test_cruceros_de_brasil_son_regionales(self):
    indexado = cruceros.set_index("cruise_id")
    
    self.assertEquals(indexado.loc[10404, "region"], "Regional")
    self.assertEquals(indexado.loc[1494, "region"], "Regional")
    self.assertEquals(indexado.loc[11099, "region"], "Regional")
    

  def test_cruceros_de_argentina_son_regionales(self):
    indexado = cruceros.set_index("cruise_id")
    
    self.assertEquals(indexado.loc[5296, "region"], "Regional")
    self.assertEquals(indexado.loc[2537, "region"], "Regional")
    self.assertEquals(indexado.loc[7237, "region"], "Regional")    
    
  def test_cruceros_de_uruguay_son_nacionales(self):
    indexado = cruceros.set_index("cruise_id")
    
    self.assertEquals(indexado.loc[5823, "region"], "Nacional")     
    
  def test_cruceros_de_usa_son_no_regionales(self):
    indexado = cruceros.set_index("cruise_id")
    
    self.assertEquals(indexado.loc[8829, "region"], "No regional")        
    

  def test_cruceros_de_otro_pais_de_asia_son_no_regionales(self):
    indexado = cruceros.set_index("cruise_id")
    
    self.assertEquals(indexado.loc[7638, "region"], "No regional")        
        