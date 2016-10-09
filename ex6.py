#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 二叉树遍历

class TreeNode(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Btree(object):
    def __init__(self, root):
        self.root = root

    def preOrder(self, node):
        """
        前序遍历  根--》左--》右
        :param node:
        :return:
        """
        if node is None:
            return
        print(node.data)
        self.preOrder(node.left)
        self.preOrder(node.right)

    def midOrder(self, node):
        """中序遍历 左--》根--》右"""
        if node is None:
            return
        self.preOrder(node.left)
        print(node.data)
        self.preOrder(node.right)
    def postOrder(self,node):
        """后序遍历 左--》右--》根"""
        if node is None:
            return
        self.preOrder(node.left)
        self.preOrder(node.right)
        print(node.data)


#实例化生成树结构
n1 = TreeNode(1)
n2 = TreeNode(2, n1)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(n3, n4)
n6 = TreeNode(6, left=n2, right=n5)
n7 = TreeNode(7)
n8 = TreeNode(8, n7, n6)
root = TreeNode('root', n7, n8)

bt = Btree(root)
print("------preOrder-------")
bt.preOrder(bt.root)
print("------midOrder-------")
bt.midOrder(bt.root)
print("------postOrder-------")
bt.postOrder(bt.root)



