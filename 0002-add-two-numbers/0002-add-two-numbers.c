/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int len(struct ListNode *list) {
        int len = 0;
    while (list != NULL) {
        len++;
        list = list->next;
    }
    return len;
}

struct ListNode *level(struct ListNode *list, int level) {
    if (list == NULL) {
        return NULL;
    }
    
    struct ListNode *tail = list; // Store the tail of the original list
    
    while (tail->next != NULL) {
        tail = tail->next;
    }
    
    for (int i = 0; i < level; i++) {
        struct ListNode *node = (struct ListNode *)malloc(sizeof(struct ListNode));
        node->val = 0;
        node->next = NULL;
        tail->next = node;  // Connect the new node to the end of the list
        tail = node;       // Update the tail to the newly created node
    }
    
    return list;
}

struct ListNode *addTwoNumbers(struct ListNode *l1, struct ListNode *l2) {
    struct ListNode *dummyHead = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *current = dummyHead;
    int carry = 0;
    
    while (l1 != NULL || l2 != NULL) {
        int sum = carry;
        if (l1 != NULL) {
            sum += l1->val;
            l1 = l1->next;
        }
        if (l2 != NULL) {
            sum += l2->val;
            l2 = l2->next;
        }
        
        carry = sum / 10;
        
        struct ListNode *node = (struct ListNode *)malloc(sizeof(struct ListNode));
        node->val = sum % 10;
        node->next = NULL;
        current->next = node;
        current = node;
    }
    
    if (carry > 0) {
        struct ListNode *node = (struct ListNode *)malloc(sizeof(struct ListNode));
        node->val = carry;
        node->next = NULL;
        current->next = node;
    }
    
    struct ListNode *result = dummyHead->next;
    free(dummyHead);
    
    return result;
}