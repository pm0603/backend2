from urllib.parse import urlencode, quote_plus, unquote
from urllib.request import urlopen, Request

import dateutil.parser
import xmltodict
from rest_framework.response import Response
from rest_framework.views import APIView

from config.settings import config
from content_api.models import Content

decode_key = unquote(config['API']['API_key'])
global_url = 'http://www.culture.go.kr/openapi/rest/publicperformancedisplays/'


# 상세 정보 저장 함수

def detail_get(seq):
    url = global_url + 'd/'
    queryParams = '?' + urlencode({quote_plus('ServiceKey'): decode_key,
                                   quote_plus('seq'): seq})

    url_query = Request(url + queryParams)
    url_query.get_method = lambda: 'GET'
    response_body = urlopen(url_query).read()
    data = xmltodict.parse(response_body)
    # 상세 정보 DB 저장
    item_path = data['response']['msgBody']['perforInfo']

    price = item_path['price']
    content = item_path['contents1']
    ticket_url = item_path['url']
    phone = item_path['phone']
    place_url = item_path['placeUrl']
    place_addr = item_path['placeAddr']
    place_seq = item_path['placeSeq']

    Content.objects.filter(seq=seq).update(
        ticket_url=ticket_url,
        phone=phone,
        price=price,
        content=content,
        place_url=place_url,
        place_addr=place_addr,
        place_seq=place_seq,
    )
    return Response(data)


# xml을 parser 후 db 저장
def xml_parser_db_save(request):
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()
    data = xmltodict.parse(response_body)

    item_path = data['response']['msgBody']['perforList']

    for index, item in enumerate(item_path):
        item_path_index = item_path[index]
        seq = item_path_index['seq']
        title = item_path_index['title']
        place = item_path_index['place']
        start_date = item_path_index['startDate']
        start_date_parse = dateutil.parser.parse(start_date).date()
        end_date = item_path_index['endDate']
        end_date_parse = dateutil.parser.parse(end_date).date()
        realm_name = item_path_index['realmName']
        area = item_path_index['area']
        thumbnail = item_path_index['thumbnail']
        gps_x = item_path_index['gpsX']
        gps_y = item_path_index['gpsY']

        Content.objects.get_or_create(
            seq=seq,
            title=title,
            place=place,
            start_date=start_date_parse,
            end_date=end_date_parse,
            realm_name=realm_name,
            area=area,
            thumbnail=thumbnail,
            gps_x=gps_x,
            gps_y=gps_y,
        )
        detail_get(seq)
    return data


# 지역을 검색시 동작
class Area(APIView):
    def get(self, request):
        keyword = request.GET.get('keyword')
        rows = request.GET.get('rows', default=10)
        url = global_url + 'area'
        queryParams = '?' + urlencode({quote_plus('ServiceKey'): decode_key,
                                       quote_plus('sido'): keyword,
                                       quote_plus('gugun'): '',
                                       quote_plus('rows'): rows})
        """
        sido = 지역 (서울, 대구, 등..)
        gugun = 구/군 (Null)으로 하면 결과가 더 잘나옴.
        """
        url_query = Request(url + queryParams)
        data = xml_parser_db_save(url_query)
        return Response(data)


# 분야별로 검색시 동작
class Genre(APIView):
    def get(self, request):
        code = request.GET.get('code')
        rows = request.GET.get('rows', default=10)
        url = global_url + 'realm'
        queryParams = '?' + urlencode({quote_plus('ServiceKey'): decode_key,
                                       quote_plus('realmCode'): code,
                                       quote_plus('rows'): rows})
        """
        A = 연극
        B = 음악 국악 콘서트
        C = 무용
        D = 미술
        """
        url_query = Request(url + queryParams)
        data = xml_parser_db_save(url_query)
        return Response(data)

# 기간별 검색시 동작
# 검색 조건과 결과가 공공데이터에서 오는 값들도 불분명해서 일단 주석처리합니다
# class Period(APIView):
#     def get(self, request):
#         start = request.GET.get('start')
#         end = request.GET.get('end')
#         rows = request.GET.get('rows', default=10)
#         url = global_url + 'period'
#         queryParams = '?' + urlencode({quote_plus('ServiceKey'): decode_key,
#                                        quote_plus('from'): start,
#                                        quote_plus('to'): end,
#                                        quote_plus('rows'): rows})
#         """
#         from = 공연 시작일
#         to = 공연 종료일
#         """
#         url_query = Request(url + queryParams)
#         data = xml_parser_db_save(url_query)
#         return Response(data)
