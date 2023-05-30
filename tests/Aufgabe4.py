OK_FORMAT = True

test = {   'name': 'Aufgabe 4',
    'points': 10,
    'suites': [   {   'cases': [   {   'code':  '>>> assert_true(np.array_equal(pl, [0.43,0.41,0.39,0.37,0.35,0.33,0.31,0.29,0.27,0.25]))\n'
                                                '>>> assert_true(np.array_equal(AU, [1.00168,0.96585,0.92997,0.89424,0.85784,0.82050,0.78402,0.74714,0.71115,0.67496]))\n'
                                                '>>> assert_equal(eps,0.66700)\n'
                                                '>>> assert_equal(slope,1.81985)\n'
                                                '>>> assert_equal(r_square,lr_res.score(np.array(pl).reshape(-1,1),AU))\n'
                                                '>>> assert_equal(conc, slope/(eps/10))\n'
                                                '>>> assert_true(np.array_equal(pl_genau,np.arange(0.37,0.42,step=0.01)))\n'
                                                '>>> assert_true(np.array_equal(prediction,lr_res.predict(pl_genau.reshape(-1,1))))\n'
                                                '>>> assert_true(np.array_equal(lsg_conc,[1,2]))\n'
                                                '>>> assert_true(np.array_equal(lsg_au,[2]))\n'
                                                '>>> assert_true(np.array_equal(lsg_delta,[1,2]))\n'
                                                '>>> assert_equal(MSE_4,(1+r_square)*np.var(AU))\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
