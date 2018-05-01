
for epo in range(opt.nepo):
    for itr, (data,label) in enumerate(dataloader):
        #=================================
        # (1) update Discriminator :
        #  maximize log D(x) + log (1 - D(G(z))
        #  = minimize -1* (log D(x) + log( 1- D(G(z)))
        #=================================
        optimizer_netD.zero_grad()
        real_data_cpu = data
        real_data = data.to(device)

        label = torch.full((opt.batchSize,), 1, device=device)
        output = netD(real_data)
        loss_Real = criterion(output,label)

        label = label.fill_(0) #<--
        loss_Real.backward()

'''
    allow_unreachable=True)  # allow_unreachable flag
RuntimeError: one of the variables needed for gradient computation has been modified by an inplace operation
'''
