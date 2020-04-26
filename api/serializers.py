from rest_framework import serializers
from .models import User, MyUser, Product, Order, Manufacturer, Delivery, Review


# MyUser 모델은 User 객체의 OneToOneField 로 생성했다.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        '''
        사용자가 처음 가입시에 패스워드를 입력하지만, 사용자 프로필페이지에서는 패스워드 데이터를 보여주면 안 된다. 
        그렇기 때문에 ModelSerializer 에서 extra_kwargs 내부에 write_only 설정을 추가하여 해당 데이터를 직렬화시 포함시키지 않을 수 있다. 
        '''
        extra_kwargs = {
                        "password": {"write_only": True},
                        }


class MyUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        # What model you're trying to serialize
        model = MyUser
        # fields = '__all__'
        fields = ('user', 'name', 'phone', 'gender', 'date_joined', 'address', 'date_of_birth', 'product')
        extra_kwargs = {
                        "date_joined": {"read_only": True},
                        "product": {"read_only": True}
                        }

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User(
            email=user_data['email'],
            username=user_data['username']
        )
        user.set_password(user_data['password'])
        user.save()
        myuser = MyUser.objects.create(**validated_data)
        return myuser


class ProductSerializer(serializers.ModelSerializer):
    # SerializerMethodField
    sales_vol = serializers.SerializerMethodField()

    class Meta:
        model = Product
        # fields 에 sales_vol 추가
        fields = ('pro_num', 'pro_name', 'inventory', 'price', 'manufacturer', 'supply_date', 'supply_vol', 'sales_vol')
        # fields = '__all__' 

    # get_{field_name} METHOD
    def get_sales_vol(self, obj):
        return obj.supply_vol - obj.inventory


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('myuser', 'product', 'quantity', 'destination', 'date_ordered', 'message')
        extra_kwargs = {"date_ordered": {"read_only": True}}


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('manu_num', 'manu_name', 'phone', 'address', 'supervisor')


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ('delivery_num', 'order', 'date_delivered', 'transport', 'state')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('review_num', 'myuser', 'order', 'title', 'image', 'content', 'pub_date')
        extra_kwargs = {"pub_date": {"read_only": True}}


