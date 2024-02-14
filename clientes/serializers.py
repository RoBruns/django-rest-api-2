from rest_framework import serializers

from clientes.models import Cliente
from clientes.validators import (validate_celular, validate_cpf, validate_nome,
                                 validate_rg)


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not validate_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf': 'O CPF deve ter 11 dígitos'}) # noqa

        if not validate_rg(data['rg']):
            raise serializers.ValidationError({'rg': 'O RG deve ter 9 dígitos'}) # noqa

        if not validate_celular(data['celular']):
            raise serializers.ValidationError({'celular': 'O celular deve ter 14 dígitos'}) # noqa

        if not validate_nome(data['nome']):
            raise serializers.ValidationError({'nome': 'Não inclua números neste campo'}) # noqa

        return data
