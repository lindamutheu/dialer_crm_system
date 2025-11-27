from rest_framework import serializers
from .models import Call, CallQueue, CallSchedule, CallDisposition, CallStatistic, CallCampaign, CallRecording
from Accounts.serializers import UserProfileSerializer

class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = '__all__'

class CallQueueSerializer(serializers.ModelSerializer):
    agents = UserProfileSerializer(many=True, read_only=True)

    class Meta:
        model = CallQueue
        fields = '__all__'

class CallScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallSchedule
        fields = '__all__'

class CallDispositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallDisposition
        fields = '__all__'

class CallStatisticSerializer(serializers.ModelSerializer):
    agent = UserProfileSerializer(read_only=True)

    class Meta:
        model = CallStatistic
        fields = '__all__'

class CallCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallCampaign
        fields = '__all__'

class CallRecordingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallRecording
        fields = '__all__'

        class AgentStatusSerializer(serializers.ModelSerializer):
            agent = UserProfileSerializer(read_only=True)

            class Meta:
                model = AgentStatus
                fields = '__all__'

                