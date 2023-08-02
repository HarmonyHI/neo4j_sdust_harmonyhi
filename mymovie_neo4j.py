from py2neo import *


def connect():
    return Graph("neo4j://localhost:7687", auth=("neo4j", "Hc766443"))


def run_sql(G, string):
    return G.run(string)


def delete_all(G):
    G.delete_all()


def get_all_node(G):
    return run_sql(G, "MATCH(n) RETURN n;")


def demo(G):
    head = Node("head_label", name='head_name')
    tail = Node("tail_label", name='tail_name')
    relation = Relationship(head, "relation_name", tail)
    G.create(relation)


# 0.
# 清除数据库
# match(n)
# detach
# delete
# n;
#
#
# 1.
# 查询数据库
# match(n)
# where n. '类型' = '喜剧'
# return n;
#
# 2.
# 查询某种电影
#     MATCH(r:'喜剧’)
#     RETURN R;
#
# 3.
# 两个演员之间的联系
# MATCH
# P = shortestPath(
#     (fb1:演员{姓名:"约瑟夫·高登-莱维特"})-[*1..50]-(fb2:演员{姓名:"凯特·温丝莱特"}) )
#     RETURN P;
#
# 4.
# 查询某人在某电影中饰演的角色
# MATCH
# (n:演员{姓名:"莱昂纳多·迪卡普里奥"}) -[r: 饰演]-> (m:电影{中文名称:"盗梦空间"})
# RETURN r.角色;
#
# 5.
# 查询某人导演的电影
# MATCH
# (n:导演{姓名:"詹姆斯·卡梅隆"}) -[r1: 导演]-> (m:电影)
# RETURN m.中文名称;
#
# 6.
# 查询编剧电影
# MATCH (n:编剧{姓名:"姜文"}) -[r1: 编剧]-> (m:电影)
# RETURN m.中文名称;
#
# 7.
# 查询演员饰演电影
# MATCH (n:演员{姓名:"葛优"}) -[r: 饰演]-> (m:电影)
# RETURN m.中文名称, r.角色;
#
# 8.
# 查询参演某电影所有演员
# MATCH (n:演员) -[r: 饰演] -> (m:电影{中文名称:"盗梦空间"})
# RETURN n.姓名;
#
#
# 9.
# 查询某个角色在某电影中的演员
# MATCH (n:演员{姓名:"莱昂纳多·迪卡普里奥"}) -[r: 饰演]-> (m:电影{中文名称:"盗梦空间"})
# RETURN r.角色;


def main():
    G = connect()
    print(str(G))
    request = 'MATCH (n) RETURN n LIMIT 2;'
    print(run_sql(G, request))


main()
