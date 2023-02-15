/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head){
    if(head==NULL)return NULL;
    struct ListNode* temp=head,*nextnode;
    while(temp->next!=0){
        if(temp->val==temp->next->val){
            nextnode=temp->next->next;
            free(temp->next);
            temp->next=nextnode;
        }
        else
        temp=temp->next;
    }
    return head;
}