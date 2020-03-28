/*Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as 
synonymous to the previous and next pointers in a doubly-linked list.*/

// inorder dfs

/**
 * Definition for a binary tree node.
 * struct Node {
 *     int val;
 *     Node* left;
 *     Node* right;
 *     Node(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    Node* treeToDoublyList(Node* root) {
        if (!root) return NULL;
        Node *head = NULL, *pre = NULL;
        inorder(root, pre, head);
        pre->right = head;
        head->left = pre;
        return head;
    }

    void inorder(Node* node, Node*& pre, Node*& head) {
        if (!node) return;
        inorder(node->left, pre, head);
        if (!head) {
            head = node;
            pre = node;
        } else {
            pre->right = node;
            node->left = pre;
            pre = node;
        }
        inorder(node->right, pre, head);
    }
};