class Test(unittest.TestCase):
  def test_loc_code_foi_renomeada(self):
    self.assertFalse("loc_code" in cinemas, "a coluna loc_code não deve mais existir")
    self.assertTrue("city_id" in cinemas, "column city_id deve existir agora")

  def test_prov_id_foi_renomeada(self):
    self.assertFalse("prov_id" in cinemas, "coluna prov_id não deve mais existir")
    self.assertTrue("province_id" in cinemas, "a coluna província_id deve existir agora")
  
  def test_dep_id_foi_renomeada(self):
    self.assertFalse("dep_id" in cinemas, "coluna dep_id não deve mais existir")
    self.assertTrue("department_id" in cinemas, "a coluna department_id deve existir agora")