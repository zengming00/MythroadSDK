t = []
t.append("16bitλͼ����")
t.append("256ɫλͼ����")
t.append("16ɫλͼ����")
t.append("GIFתλͼ����")
t.append("JPGתλͼ����")
t.append("�˳���ʾ")

for s in t:
  uni = s.decode("cp936")
  u = ''
  for c in uni:
    c = ord(c)
    u = u + '\\' + hex(c / 256)[1:] + '\\' + hex(c % 256)[1:]
  print s
  print u