import pyo
s = pyo.Server().boot()
s.start()

wav = pyo.SquareTable()
env = pyo.CosTable([(0, 0), (100, 1), (500, .3), (8191, 0)])
met = pyo.Metro(.125, 12).play()
amp = pyo.TrigEnv(met, table=env, mul=.1)
pit = pyo.TrigXnoiseMidi(met, dist='loopseg', x1=20, scale=1, mrange=(48, 84))
out = pyo.Osc(table=wav, freq=pit, mul=amp).out()

rec = pyo.Record(out, filename='entropy.wav', chnls=1, fileformat=0, sampletype=1)

clean = pyo.Clean_objects(10.1, rec)
clean.start()
