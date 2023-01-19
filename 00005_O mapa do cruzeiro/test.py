class Test(unittest.TestCase):

  def test_cruzeiros_contem_coluna_region(self):
    self.assertTrue("region" in cruzeiros.columns)

  def test_cruzeiros_do_brasil_são_regionais(self):
    indexado = cruzeiros.set_index("cruise_id")
    
    self.assertEquals(indexado.loc[10404, "region"], "Regional")
    self.assertEquals(indexado.loc[1494, "region"], "Regional")
    self.assertEquals(indexado.loc[11099, "region"], "Regional")
    

  def test_cruzeiros_da_argentina_são_regionais(self):
    indexado = cruzeiros.set_index("cruise_id")
    
    self.assertEquals(indexado.loc[5296, "region"], "Regional")
    self.assertEquals(indexado.loc[2537, "region"], "Regional")
    self.assertEquals(indexado.loc[7237, "region"], "Regional")
    
  def test_cruzeiros_do_uruguai_são_nacionais(self):
    indexado = cruzeiros.set_index("cruise_id")
    
    self.assertEquals(indexado.loc[5823, "region"], "Nacional")
    
  def test_cruzeiros_do_uea_são_nan(self):
    indexado = cruzeiros.set_index("cruise_id")
    
    self.assertTrue(pd.isna(indexado.loc[8829, "region"]))