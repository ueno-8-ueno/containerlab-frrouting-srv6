# README
- 以下の内容は
本来OSPFv3により「r1->r2->r3」と辿るところを「r1->r5->r6->r3」と
経路を変更するためのものです.
---

## SRポリシーの追加(例)
```bash
# r1コンテナのbashで実行
ip -6 route add 2001:db8:7::/64 encap seg6 mode encap segs 2001:db8:2::2,2001:db8:5::2,2001:db8:6::2 dev eth2
```

## コンテナの外からtcpdumpでキャプチャ(CONTAINER IDは適宜書き換える)
```bash
# コンテナ外で実行
# この場合, r1のeth2を通る通信が対象
# CONTAINER IDは docker psコマンドで確認
sudo nsenter -n -t $(docker inspect --format {{.State.Pid}} <CONTAINER ID>) -- tcpdump -i eth2 -w test.pcap
```

## pingによる疎通確認(キャプチャ用)
```bash
# r1コンテナのbashで実行
ping 2001:db8:7::2
```

## SRポリシーの削除(例)
```bash
# r1コンテナのbashで実行
ip -6 route del 2001:db8:7::/64
```