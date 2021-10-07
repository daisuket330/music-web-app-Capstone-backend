

class CommentSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentSection
        fields = ['id','comment','video_id', 'like', 'dislike']

       
class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['reply_text', 'repliedcomment']