

def test_end_to_end():

    # setup our config
    config = CasConfig()

    # read in for the tester process the development files
    config.update('tester', 'development')

    # assert what we know should be present
    assert config.get('root') == 1
    assert config.get('wsgi',{}).get('wsgi_found') == 1
    assert config.get('in_proc') == 1
    assert config.get('extras') == 'fun'

