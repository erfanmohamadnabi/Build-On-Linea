from django.shortcuts import render
from dune_client.client import DuneClient
from .models import Data

# Create your views here.

API_KEY = 't0S9A3xCz0kIHVZqgIjAiUclkAuQUDtW'
NFT_API_KEY = 'zeWCimbw8U2VHwu66g7dRMnBGcQyeNJB'

#* LXP API VIEW

[{'LXP': '5451', 'NFTs': '4', 'rank': 5994, 'wallet': '0x545425f9686b56078da3bfac5f9f25bb287b1291'}]

def Index(request):



    context = {
                'user_lxp': 0,
                    'user_nfts': 0,
                    'user_rank': 0,
                }

    if request.POST:

        address = request.POST.get("address")

        #! GET LXP

        dune_lxp = DuneClient(API_KEY)
        response = dune_lxp.get_custom_endpoint_result(
        "test123222",
        "test1234",
        limit=10,
        filters = f"wallet = '{address}'"
        )
        rows = response.result.rows
        print(rows)

        if rows:
            user_lxp = rows[0]['LXP']
            user_nfts = rows[0]['NFTs']
            user_rank = rows[0]['rank']

            request.session['user_lxp'] = user_lxp
            request.session['user_nfts'] = user_nfts
            request.session['user_rank'] = user_rank

            request.session['total'] = user_nfts

            new_data = Data.objects.create(
                address = address,
                lxp = user_lxp,
                rank = user_rank,
                nfts = user_nfts
            )

            new_data.save()
            if request.session.get('user_lxp'):
                context = {
                'user_lxp': request.session.get('user_lxp'),
                    'user_nfts': request.session.get('user_nfts'),
                    'user_rank': request.session.get('user_rank'),
                }
            else:
                context = {
                'user_lxp': 0,
                    'user_nfts': 0,
                    'user_rank': 0,
                }


        #! GET NFTs

        dune_nft = DuneClient(NFT_API_KEY)
        response = dune_nft.get_custom_endpoint_result(
        "test123222",
        "nft",
        limit=10,
        filters = f"address = '{address}'"
        )
        rows = response.result.rows

        

        if rows:
            alpha = rows[0]['token_id_1']
            beta = rows[0]['token_id_2']
            gamma = rows[0]['token_id_3']
            delta = rows[0]['token_id_4']
            omega = rows[0]['token_id_5']

            request.session['alpha'] = alpha
            request.session['beta'] = beta
            request.session['gamma'] = gamma
            request.session['delta'] = delta
            request.session['omega'] = omega
        else:
            request.session['alpha'] = 0
            request.session['beta'] = 0
            request.session['gamma'] = 0
            request.session['delta'] = 0
            request.session['omega'] = 0
            request.session['total'] = 0
            


        print(rows)
        


    return render(request,'index.html',context)


def Nft(request):
    if request.session.get('alpha'):
        context = {
            'alpha': request.session.get('alpha'),
            'beta': request.session.get('beta'),
            'gamma': request.session.get('gamma'),
            'delta': request.session.get('delta'),
            'omega': request.session.get('omega'),
            'total': request.session.get('total'),
        }
    else:
        context = {
            'alpha':0,
            'beta': 0,
            'gamma': 0,
            'delta': 0,
            'omega': 0,
            'total': 0,
        }

    return render(request,'nft.html',context)


def About_Us(request):
    context = {}

    

    return render(request,'about.html',context)


[{'address': '0x545425f9686b56078da3bfac5f9f25bb287b1291', 'token_id_1': '1', 'token_id_2': '1', 'token_id_3': '1', 'token_id_4': '0', 'token_id_5': '1'}]