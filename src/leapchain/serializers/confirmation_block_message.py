from rest_framework import serializers

from leapchain.constants.network import BLOCK_IDENTIFIER_LENGTH
from leapchain.serializers.account_balance import AccountBalanceSerializer
from leapchain.serializers.network_block import NetworkBlockSerializer


class ConfirmationBlockMessageSerializer(serializers.Serializer):
    block = NetworkBlockSerializer()
    block_identifier = serializers.CharField(max_length=BLOCK_IDENTIFIER_LENGTH)
    updated_balances = AccountBalanceSerializer(many=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
